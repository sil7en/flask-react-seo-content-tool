from nlp.index import nlpMain
from lib.flask_scraper import flaskscraper_main
import os
from dotenv import load_dotenv

# init dotenv to  use variables from .env file
load_dotenv()

def appMain(keyword):

    # First step: execute flaskscraper_main
    # Check if there is data about the keyword.
    # If there is some then return it.
    # If data doesn't exist, scrape it.

    # init project vars from .env
    env_project_path = os.getenv('PATH_PROJECT_FOLDER')
    env_googlegeo = os.getenv('GOOGLE_GEO')
    env_googleurl = os.getenv('GOOGLE_URL')

    # call to flaskscraper_main()
    res_scraper = flaskscraper_main(keyword, env_googlegeo, env_googleurl, env_project_path)

    # simple call to nlp index function
    #nlpMain(keyword)

    return res_scraper