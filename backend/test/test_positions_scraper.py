import sys
sys.path.append('../')
from goo_positions_scraper.index import positionsScraper

main_keyword = 'seguro automotriz'

if __name__ == "__main__":
    test_scraper = positionsScraper(main_keyword)
    print(test_scraper)