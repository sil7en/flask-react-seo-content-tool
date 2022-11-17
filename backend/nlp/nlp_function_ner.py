import spacy
#!python -m spacy download es_core_news_lg

nlp = spacy.load('es_core_news_lg')
def nlp_function_ner(arr):
    arr_return = []

    for text in arr:
        arr_except = ['', ' ']
        if text not in arr_except:
            doc_nlp = nlp(text)
            entities = doc_nlp.ents
            for ent in entities:
                if ent.text not in arr_except:
                    arr_return.append(ent.text)

    return arr_return