import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

stopword_es = nltk.corpus.stopwords.words('spanish')

def nlp_function_nostopwords(arr):
    arr_return = []
    for text in arr:
        text_split = text.split()
        arr_nostopwords = [word for word in text_split if word not in stopword_es]
        str_nostopwords = ' '.join(arr_nostopwords)

        arr_except = ['', ' ']
        if str_nostopwords not in arr_except:
            arr_return.append(str_nostopwords)
    
    return arr_return