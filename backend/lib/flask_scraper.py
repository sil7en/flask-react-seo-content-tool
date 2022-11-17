import sys
sys.path.append('../')
from goo_search_scraper.goo_main import gooMain
from goo_trends_scraper.goot_main import gootMain
from goo_positions_scraper.index import positionsScraper
from lib.json_export import json_export
import os

def flaskscraper_main(keyword: str, googleGeo: str, googleurl: str, project_path: str):

    # First step
    # Check if there is data about the keyword.
    path_folder_keyword = f'{project_path}/JSON/{keyword}'
    # path exists or not
    path_folder_keyword_isExist = os.path.exists(path_folder_keyword)
    
    # boolean to decide next steps
    # If there is some then return it.
    if path_folder_keyword_isExist == True:
        data_return = 'The data exist'

    # If data doesn't exist, scrape it.
    else:
        data_return = "No data yet. The scraper already start."

        gooTrends = gootMain(keyword, googleGeo)
        gooSearch = gooMain(keyword, googleurl)

        # call to export_json function over gooSearch and gooTrends
        json_export(gooSearch, 'gsearch')
        json_export(gooTrends, 'gtrends')

        # Var to store top position websites' text data
        top_positions_textData = positionsScraper(keyword)
        json_export(top_positions_textData, 'gsearch')
        

    # obj to return data to Flask
    obj_return = {
        'data': data_return
    }

    return obj_return



#def examplefunction(keyword: str, googleGeo: str, googleurl: str):
    #gooTrends = gootMain(keyword, googleGeo)
    #gooSearch = gooMain(keyword, googleurl)
    
    # call to export_json function over gooSearch and gooTrends
    #json_export(gooSearch, 'gsearch')
    #json_export(gooTrends, 'gtrends')

    # Var to store top position websites' text data
    #top_positions_textData = positionsScraper(keyword)
    #json_export(top_positions_textData, 'gsearch')