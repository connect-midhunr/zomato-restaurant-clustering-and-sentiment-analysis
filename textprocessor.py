# importing libraries for text processing
import re
import nltk
from stop_words import get_stop_words
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
nltk.download('wordnet')
import pickle

# defining a function for text tokenization and stopword removal
def tokenize(text: str):
  """
  Function to carry out tokenization and stopword removal of text data
  """

  # converting from object to string
  mod_text = str(text)

  # removing punctuations
  mod_text = re.sub('[^a-zA-Z]', ' ', mod_text)
  print('mod_text:', mod_text)

  # converting all characters to lower case and splitting into words
  text_array = mod_text.lower().split()
  print('text_array:', text_array)

  # removing stopwords
  text_array = [word for word in text_array if word not in get_stop_words('english')]
  print('text_array:', text_array)

  return text_array

# defining a function for stemming text
def stemming(text_array: list):
    """
    Function for stemming text
    """
    lemmatizer = WordNetLemmatizer()
    return ' '.join([lemmatizer.lemmatize(word) for word in text_array])

# define a function for vectorizing text
def vectorize(text: str, vectorizer):
    """
    Function to vectorize text
    """
    text_matrix = vectorizer.transform([text])
    return text_matrix

# defining a function for text processing
def process_text(text: str, vectorizer: WordNetLemmatizer):
    """
    Function to process text for sentiment predict
    """
    print('text:', text)
    text_array = tokenize(text)
    print('text_array:', text_array)
    text = stemming(text_array)
    print('text:', text)
    return vectorize(text, vectorizer)

# def main():
#     vectorizer = pickle.load(open('./models/text_vectorizer.pkl', 'rb'))
#     text = 'decided grub monday afternoon dashed frio bistro particular reason many customer around definitely helped u get attention service ok carefully curated order chimichuri pan fried fish lamb ravioli andhra pepper chicken pizza must say food tasted authentic delicious chimichuri pan fried fish chef s special came fish boasting tangy spicy herb crust salsa sauteed spinach scallion rice easily best dish ordered lamb ravioli creamy searching minced meat therein came spicy andhra pepper chicken pizza generated interest despite diminishing appetite place come across expensive item portion size worth visit made another visit uploading picture'
#     print(process_text(text, vectorizer))

# if __name__ == '__main__':
#     main()