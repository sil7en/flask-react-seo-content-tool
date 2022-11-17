import json
from time import gmtime, strftime
import os
from dotenv import load_dotenv

# init dotenv to  use variables from .env file
load_dotenv()

# Function to iterate arr and export json files
# data_origin options: "gsearch" or "gtrends"
def json_export(obj, data_origin: str):
    project_path = os.getenv('PATH_PROJECT_FOLDER')

    # var to store keyword_with_no_spaces created
    keyword_obj = obj.pop('keyword')
    
    # get the NOW time
    time_now = strftime("%Y-%m-%d", gmtime())

    # main iteration over main obj
    for key, value in obj.items():
        data_type = key
        data_object = {
            'keyword': keyword_obj,
            'dataOrigin': data_origin,
            'dataType': data_type,
            'date': time_now,
            'data': value
        }

        # Path to export file defined and created as dir with os
        path_export = f'{project_path}/JSON/{keyword_obj}/{data_origin}/{data_type}/{time_now}.json'
        os.makedirs(os.path.dirname(path_export), exist_ok=True)
        
        # Export files process START
        with open(path_export, 'w', encoding='utf-8') as f:
            json.dump(data_object, f, ensure_ascii=False)