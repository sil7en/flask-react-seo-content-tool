import json
import time
from time import gmtime, strftime
import sys
sys.path.append('../')
from goo_search_scraper.goo_main import gooMain
from goo_trends_scraper.goot_main import gootMain
from goo_positions_scraper.index import positionsScraper
from nlp.index import nlpMain
import os

main_keyword = 'vajilla'
googleGeo = 'CL'
googleurl = 'http://www.google.cl/'
project_path = 'c:/dev/dev-projects/seo-content-tool'


if __name__ == "__main__":
    gooTrends = gootMain(main_keyword, googleGeo)
    gooSearch = gooMain(main_keyword, googleurl)

    # Function to iterate arr and export json files
    # data_origin options: "gsearch" or "gtrends"
    def export_json(obj, data_origin: str):
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
            path_export = f'{project_path}/json_local/{keyword_obj}/{data_origin}/{data_type}/{time_now}.json'
            os.makedirs(os.path.dirname(path_export), exist_ok=True)
            
            # Export files process START
            with open(path_export, 'w', encoding='utf-8') as f:
                json.dump(data_object, f, ensure_ascii=False)

    
    # call to export_json function over gooSearch and gooTrends
    export_json(gooSearch, 'gsearch')
    export_json(gooTrends, 'gtrends')

    # Var to store top position's text data
    top_positions_textData = positionsScraper(main_keyword)
    export_json(top_positions_textData, 'gsearch')

    # simple call to nlp index function
    nlpMain(main_keyword)