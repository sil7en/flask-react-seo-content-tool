import sys
sys.path.append('../')
from goo_trends_scraper.goot_main import gootMain

googleGeo = 'CL'
main_keyword = 'seguro automotriz'


if __name__ == "__main__":
    test_query = gootMain(main_keyword, googleGeo)