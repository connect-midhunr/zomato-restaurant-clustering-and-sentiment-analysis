import uvicorn
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import pickle
from textprocessor import process_text

# loading model
model = pickle.load(open('./models/sentiment_model.pkl', 'rb'))

# initializing app
app = FastAPI()

# initializing jinja2 templates and static files
templates = Jinja2Templates(directory='./templates')
app.mount('/static', StaticFiles(directory='./static'), 'static')

# defining index page
@app.get('/')
def index(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})

# defining prediction api for sentiment analysis
@app.post('/predict_sentiment')
def predict_sentiment(request: Request, text: str = Form(...)):
    processed_text = process_text(text)
    if model.predict(processed_text)[0] == 1:
        sentiment = 'Positive'
    else:
        sentiment = 'Negative'
    return templates.TemplateResponse('index.html', {'request': request, 'review': "\"" + text + "\"", 'sentiment': sentiment})

if __name__ == '__main__':
    uvicorn.run(app)