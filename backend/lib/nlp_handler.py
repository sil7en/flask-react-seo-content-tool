from nlp.index import nlpMain
import sys
sys.path.append('../')
from lib.json_export import json_export
import os
from dotenv import load_dotenv

# init dotenv to  use variables from .env file
load_dotenv()

def nlp_handler(keyword, res_scraper):
    if res_scraper['dataExist'] == True:
        # first step: check if nlp data exist
        env_project_path = os.getenv('PATH_PROJECT_FOLDER')
        path_check_nlp_folder = f'{env_project_path}/JSON/{keyword}/gsearch/nlp_global_bow'
        check_nlp_folder_isExist = os.path.exists(path_check_nlp_folder)

        # boolean to take actions about check_nlp_folder_isExist results
        if check_nlp_folder_isExist == True:
            return {'data': True}
        else:
            nlp = nlpMain(keyword)
            # nlp: dict_keys(['keyword', 'dataOrigin', 'dataType', 'date', 'data', 'topPositionsNlpGrams', 'TextData_global_bow'])
            
            # Export nlp['TextData_global_bow'] to json file
            arr_order_global_bow = sorted(nlp['TextData_global_bow'].items(), key=lambda x: x[1], reverse=True)
            order_global_bow = [{'keyword': k, 'count': v, 'ngrams': len(k.split(' ')), 'words': k.split(' ')} for k,v in arr_order_global_bow]
            nlp['TextData_global_bow'] = order_global_bow

            obj_global_bow = {'keyword': keyword, 'nlp_global_bow': nlp['TextData_global_bow']}
            json_export(obj_global_bow, 'gsearch')

            # Export nlp['topPositionsNlpGrams'] to json file
            obj_page_bow = {'keyword': keyword, 'nlp_pages': nlp['topPositionsNlpGrams']}
            json_export(obj_page_bow, 'gsearch')
            
            return {'data': True}
    else:
        return {'data': False}