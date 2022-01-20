from bs4 import BeautifulSoup
from matplotlib.pyplot import text
from selenium.webdriver.chrome import service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from probability_model import median_of_odds_twoway

from scrap_odd_info import get_odds
from probability_model import median_of_odds
from scrap_result_odd import scrap_odds

chrome_options = webdriver.chrome.options.Options()
chrome_options.add_argument('--headless')
service_to_pass = Service(ChromeDriverManager().install())
wd = webdriver.Chrome(service = service_to_pass,options = chrome_options)

def get_outcomes(twoway,url):
    URL_EVENT = url
    wd.get(URL_EVENT)
    soup_file = wd.page_source
    soup_page = BeautifulSoup(soup_file, "html.parser")

    main_table = soup_page.find('table', {'class': 'table-main detail-odds sortable'})
    table_rows = main_table.find_all('tr')

    odds_info = get_odds(table_rows, twoway)

    print(len(odds_info))
    
    if not twoway:
        media_home, media_draw, media_away = median_of_odds(odds_info)
        return media_home, media_draw, media_away
    media_home, media_away = median_of_odds_twoway(odds_info)
    return media_home, media_away
    

def print_outcomes(twoway, url):
    if(not twoway):
        media_home, media_draw, media_away = get_outcomes(twoway,url)
        print("Home win probability: {:.2f}%".format(media_home*100))
        print("Draw probability: {:.2f}%".format(media_draw*100))
        print("Away win probability: {:.2f}%".format(media_away*100))
    else:
        media_home, media_away = get_outcomes(twoway,url)
        print("Home win probability: {:.2f}%".format(media_home*100))
        print("Away win probability: {:.2f}%".format(media_away*100))

def get_likely_result(url):
    odd_c = url + "/#cs;2"

    wd.get(odd_c)

    soup_file = wd.page_source
    soup_page = BeautifulSoup(soup_file, "html.parser")
    soup_page = soup_page.find('div', {'id': 'col-content'})

    likely_scores = scrap_odds(soup_page)

    return likely_scores

def print_likely_score(url):
    likely_scores = get_likely_result(url)
    
    print(f"Likely Score: {likely_scores.score}")


def get_final_score(url):
    URL_EVENT = url
    wd.get(URL_EVENT)
    soup_file = wd.page_source
    soup_page = BeautifulSoup(soup_file, "html.parser")
    
    result = (soup_page.find('p', {'class': 'result'})).find('strong').text
    print(f"Final Score: {result}")