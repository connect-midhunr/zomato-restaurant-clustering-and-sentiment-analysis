import uvicorn
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import pickle
from textprocessor import process_text

# loading model
model = pickle.load(open('./models/sentiment_model.pkl', 'rb'))
scaler = pickle.load(open('./models/std_scaler.pkl', 'rb'))
vectorizer = pickle.load(open('./models/text_vectorizer.pkl', 'rb'))

# initializing app
application = FastAPI()

# initializing jinja2 templates and static files
templates = Jinja2Templates(directory='./templates')
application.mount('/static', StaticFiles(directory='./static'), 'static')

# defining index page
@application.get('/')
async def index(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})

# defining prediction api for sentiment analysis
@application.post('/predict_sentiment')
async def predict_sentiment(request: Request, text: str = Form(...)):
    print('text:', text)
    processed_text = process_text(text, vectorizer)
    print('processed_text:', processed_text)
    scaled_text = scaler.transform(processed_text)
    print('scaled_text:', scaled_text)
    result = model.predict(scaled_text)
    print('result:', result)
    if result[0] == 1:
        sentiment = 'Positive'
    else:
        sentiment = 'Negative'
    return templates.TemplateResponse('index.html', {'request': request, 'review': "\"" + text + "\"", 'sentiment': sentiment})

if __name__ == '__main__':
    uvicorn.run(application)