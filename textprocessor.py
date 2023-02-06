# importing libraries for text processing
import re
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
import pickle

# defining a function for text tokenization and stopword removal
def tokenize(text):
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
def stemming(text_array):
    """
    Function for stemming text
    """
    stemmer = PorterStemmer()
    return ' '.join([stemmer.stem(word) for word in text_array])

vectorizer = pickle.load(open('./models/text_vectorizer.pkl', 'rb'))

# define a function for vectorizing text
def vectorize(text):
    """
    Function to vectorize text
    """
    text_matrix = vectorizer.transform([text])
    return text_matrix

# defining a function for text processing
def process_text(text):
    """
    Function to process text for sentiment predict
    """
    print('text:', text)
    text_array = tokenize(text)
    print('text_array:', text_array)
    text = stemming(text_array)
    print('text:', text)
    return vectorize(text)
