import re
import unidecode

def nlp_function_cleanData(arr):
    arr_return = []
    
    for text in arr:
        #text to lowercase
        text_lower = text.lower()
        # text unidecoded
        clean_text = unidecode.unidecode(text_lower)
        # text with no ¿? especial characters,
        clean_text = re.sub('[^A-Za-z0-9]', ' ', clean_text)
        # string with no numbers
        text_nonumbers = re.sub('[0-9]', '', clean_text)
        # string with no extra blank spaces
        text_nospace = " ".join(text_nonumbers.split())

        # arr to exclude words or characters
        arr_exclude = ['', ' ']

        # add final clean text to arr_return
        if text_nospace not in arr_exclude and len(text_nospace) > 1:
            arr_return.append(text_nospace)

    return arr_return