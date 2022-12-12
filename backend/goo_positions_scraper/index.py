import json
import glob
import datetime
from goo_positions_scraper.positions_webscraper import positionsWebscraper
import os
from dotenv import load_dotenv

# init dotenv to  use variables from .env file
load_dotenv()

env_project_path = os.getenv('PATH_PROJECT_FOLDER')

def positionsScraper(keyword):
    # var to store folder json's path
    json_keyword_folder_path = f'{env_project_path}/JSON/{keyword}/gsearch/top_positions/'
    all_json_files = glob.glob(f'{json_keyword_folder_path}*.json')

    # order json_files by date
    json_with_date = list(map(lambda x: {'url': x, 'date': x.split('\\')[-1].split('.')[0]}, all_json_files))
    json_files_order = sorted(json_with_date, key=lambda x: datetime.datetime.strptime(x['date'], '%Y-%m-%d'), reverse=True)
    # get the most recent json file of top positions to process data
    last_json_file_path = json_files_order[0]

    # first step is to open json file to get goo_positions
    with open(last_json_file_path['url'], 'r', encoding='utf-8') as fh:
        # Var to store object most recent file of top positions for keyword
        data_positions = json.load(fh)

    obj_return = {
        "keyword": keyword,
        'topPositionsTextData': positionsWebscraper(data_positions["data"])
    }
    
    return obj_return