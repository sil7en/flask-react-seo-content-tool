def nlp_function_bow(arr):
    obj_return = {}
    # create bag of words about arr_return
    # main iteration for bag of words
    for ngram in arr:
        if ngram not in obj_return:
            obj_return.update({ngram: 1})
        else:
            obj_return.update({ngram: int(obj_return[ngram]) + 1})

    # iteration to order obj_return by value
    obj_return_sorted = {}
    for k in sorted(obj_return, key=obj_return.get, reverse=True):
        obj_return_sorted.update({k: obj_return[k]})

    return obj_return_sorted