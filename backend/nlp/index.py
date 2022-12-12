import json
import glob
import datetime
import sys
sys.path.append('../')
from nlp.nlp_TextData import nlp_TextData
from nlp.nlp_function_bow import nlp_function_bow
from nlp.nlp_function_global_bow import nlp_function_global_bow
import os
from dotenv import load_dotenv

# init dotenv to  use variables from .env file
load_dotenv()

env_project_path = os.getenv('PATH_PROJECT_FOLDER')

def nlpMain(keyword):
    # this function works based on .json file from topPositionTextData folder

    # var to store folder json's path
    json_keyword_folder_path = f'{env_project_path}/JSON/{keyword}/gsearch/topPositionsTextData/'
    all_json_files = glob.glob(f'{json_keyword_folder_path}*.json')

    # order json_files by date
    json_with_date = list(map(lambda x: {'url': x, 'date': x.split('\\')[-1].split('.')[0]}, all_json_files))
    json_files_order = sorted(json_with_date, key=lambda x: datetime.datetime.strptime(x['date'], '%Y-%m-%d'), reverse=True)
    # get the most recent json file of topPositionTextData to process data
    last_json_file_path = json_files_order[0]

    # first step is to open json file to get goo_positions
    with open(last_json_file_path['url'], 'r', encoding='utf-8') as fh:
        # Var to store object most recent file of keyword's topPositionTextData
        data_json = json.load(fh)

    # main iteration on top positions data
    arr_return = []
    for element in data_json["data"]:
        # function to process data inside ["TextData"]
        obj_nlp_TextData = nlp_TextData(element['TextData'])
        # add obj_nlp_TextData to element to return
        element.update({'nlpGramsNer': obj_nlp_TextData})

        # function to apply global bag of words function
        arr_bow_global_grams = []
        # iteration to get all grams in one big arr
        for key, value in obj_nlp_TextData.items():
            arr_bow_global_grams.extend(value['nlpAllGrams'])
        # apply nlp_function_bow to arr_bow_global_grams
        bow_global_grams = nlp_function_bow(arr_bow_global_grams)
        # add bow_global_grams to element to return
        element.update({'nlp_bow_grams': bow_global_grams})


        # function to apply global ner bag of words function
        arr_bow_global_grams_ner = []
        # iteration to get all grams in one big arr
        for key, value in obj_nlp_TextData.items():
            arr_bow_global_grams_ner.extend(value['nlpAllNerGrams'])
        # apply nlp_function_bow to arr_bow_global_grams
        bow_global_grams_ner = nlp_function_bow(arr_bow_global_grams_ner)
        # add bow_global_grams to element to return
        element.update({'nlp_bow_grams_ner': bow_global_grams_ner})

        arr_return.append(element)

    obj_return = {
        "topPositionsNlpGrams": arr_return
    }

    data_json.update(obj_return)

    # print(data_json.keys())
    # dict_keys(['keyword', 'dataOrigin', 'dataType', 'date', 'data', 'topPositionsNlpGrams'])
    
    # data_json['topPositionsNlpGrams'] is an array of objects
    # dict_keys(['position', 'link', 'web', 'title', 'description', 'TextData', 'nlpGramsNer', 'nlp_bow_grams', 'nlp_bow_grams_ner'])
    # Example for the first arr element: print(data_json['topPositionsNlpGrams'][0]['nlp_bow_grams'])
    
    # Function to get global bow from arr data_json['topPositionsNlpGrams']
    TextData_global_bow = nlp_function_global_bow(data_json['topPositionsNlpGrams'])

    data_json.update({'TextData_global_bow': TextData_global_bow})


    return data_json
