def nlp_function_global_bow(arr):
    obj_return = {}

    # main iteration to get all grams into one large arr
    for element in arr:
        # every element has ['position', 'link', 'web', 'title', 'description', 'TextData', 'nlpGramsNer', 'nlp_bow_grams', 'nlp_bow_grams_ner']
        current_dict = element['nlp_bow_grams']
        
        # iteration over current_dict to add value key to obj_return
        for key, value in current_dict.items():
            if key not in obj_return:
                obj_return.update({key: value})
            else:
                obj_return[key] += value
    
    # iteration to order obj_return by value
    obj_return_sorted = {}
    for k in sorted(obj_return, key=obj_return.get, reverse=True):
        obj_return_sorted.update({k: obj_return[k]})

    # iteration over obj_return_sorted to remove values == 1
    obj_return_final = {}
    for key, value in obj_return_sorted.items():
        if value > 2:
            obj_return_final.update({key: value})

    print(obj_return_final)
    return obj_return_sorted