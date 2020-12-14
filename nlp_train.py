import re
import nltk
#nltk.download('stopwords')
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.externals import joblib
REPLACE_BY_SPACE_RE = re.compile('[/(){}\[\]\|@,;]')
BAD_SYMBOLS_RE = re.compile('[^0-9a-z #+_]')
STOPWORDS = set(stopwords.words('english'))

def text_prepare(text):
    text = text.lower()
    text = REPLACE_BY_SPACE_RE.sub(' ', text)
    text = BAD_SYMBOLS_RE.sub('', text)
    text = ' '.join([x for x in text.split() if x and x not in STOPWORDS])
    return text
def tfidf_predict(data):
    tfidf_vectorizer = joblib.load('Models/enthire_tfidf.pkl')
    #tfidf_vectorizer = TfidfVectorizer(min_df=5, max_df=0.9, ngram_range=(1, 2), vocabulary=tfidf_data)
    data = [text_prepare(x) for x in data]
    text_predict = tfidf_vectorizer.transform(data)
    return text_predict
def model_predict(data):
    text_predict = tfidf_predict([data])
    lr = joblib.load('Models/naive_enthire.pkl')
    y_pred = lr.predict(text_predict)
    print(y_pred)
    if(y_pred== 1):
        return "Positive"
    return "Negative"
