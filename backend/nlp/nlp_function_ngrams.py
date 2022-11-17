from nltk import ngrams

def nlp_function_ngrams(arr, number):
    arr_return = []
    obj_return = {}
    
    # main iteration to get ngrams for every text
    for text in arr:
        # var to defines how many n_grams want to obtain
        n_grams = ngrams(text.split(), number)
        # temp arr to store ngrams for any text
        arr_ngrams = []

        # iteration over n_grams zip objects tuples
        for t_gram in n_grams:
            # var to store the final string of the n_gram
            str_return = ''
            # iteration over tuples to get text of grams and stringify them
            for gram in t_gram:
                str_return += gram + ' '
            
            # clean str_return of white spaces
            str_return = " ".join(str_return.split())
            
            # append all ngrams that different from empty to arr_ngrams
            if str_return != '' and str_return != ' ':
                arr_ngrams.append(str_return)
        
        arr_return.extend(arr_ngrams)
        
    return arr_return