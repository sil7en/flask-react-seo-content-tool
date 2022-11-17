from nlp.nlp_function_cleanData import nlp_function_cleanData
from nlp.nlp_function_nostopwords import nlp_function_nostopwords
from nlp.nlp_function_ngrams import nlp_function_ngrams
from nlp.nlp_function_ner import nlp_function_ner

def nlp_TextData(data):
    obj_return = {}
    # iteration over element['TextData']
    for key, value in data.items():

        # apply functions to value data
        nlpCleanData = nlp_function_cleanData(value)
        nlpNoStopWords = nlp_function_nostopwords(nlpCleanData)
        nlpOneGrams = nlp_function_ngrams(nlpCleanData, 1)
        nlpBiGrams = nlp_function_ngrams(nlpCleanData, 2)
        nlpTriGrams = nlp_function_ngrams(nlpCleanData, 3)
        nlpOneGrams_nsw = nlp_function_ngrams(nlpNoStopWords, 1)
        nlpBiGrams_nsw = nlp_function_ngrams(nlpNoStopWords, 2)
        nlpTriGrams_nsw = nlp_function_ngrams(nlpNoStopWords, 3)
        nlpNer = nlp_function_ner(value)
        nlpNer_clean = nlp_function_cleanData(nlpNer)
        nlpOneGrams_ner = nlp_function_ngrams(nlpNer_clean, 1)
        nlpBiGrams_ner = nlp_function_ngrams(nlpNer_clean, 2)
        nlpTriGrams_ner = nlp_function_ngrams(nlpNer_clean, 3)

        # function to make bow over all grams (no entities from ner)
        arr_grams = [nlpBiGrams_nsw, nlpTriGrams_nsw]
        arr_all_grams = []
        for grams in arr_grams:
            arr_all_grams.extend(grams)

        # function to make bow over all grams from ner
        arr_grams_ner = [nlpBiGrams_ner, nlpTriGrams_ner, nlpNer]
        arr_all_grams_ner = []
        for grams_ner in arr_grams_ner:
            arr_all_grams_ner.extend(grams_ner)

        obj_return.update({
            key: {
                #'rawData': value,
                'nlpOneGrams': nlpOneGrams,
                'nlpBiGrams': nlpBiGrams,
                'nlpTriGrams': nlpTriGrams,
                'nlpOneGrams-nsw': nlpOneGrams_nsw,
                'nlpBiGrams-nsw': nlpBiGrams_nsw,
                'nlpTriGrams-nsw': nlpTriGrams_nsw,
                'nlpNer': nlpNer_clean,
                'nlpOneGrams-ner': nlpOneGrams_ner,
                'nlpBiGrams-ner': nlpBiGrams_ner,
                'nlpTriGrams-ner': nlpTriGrams_ner,
                'nlpAllGrams': arr_all_grams,
                'nlpAllNerGrams': arr_all_grams_ner
            }
        })

    return obj_return