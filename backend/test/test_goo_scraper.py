import sys
sys.path.append('../')
from goo_search_scraper.goo_main import gooMain

googleurl = 'http://www.google.cl/'
main_keyword = 'seguro automotriz'


if __name__ == "__main__":
    test_query = gooMain(main_keyword, googleurl)