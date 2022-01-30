from doctest import script_from_examples
import os

from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

from probability_model import median_of_odds_twoway
from writer import write_header, write_odds, write_score
from scrap_odd_info import get_odds

chrome_options = webdriver.chrome.options.Options()
chrome_options.add_argument('--headless')
service_to_pass = Service(ChromeDriverManager().install())
wd = webdriver.Chrome(service = service_to_pass,options = chrome_options)

URL_BASE = "https://www.oddsportal.com"
URL_EVENT = URL_BASE + "/basketball/usa/nba-2020-2021/results/"

wd.get(URL_EVENT)
soup_file = wd.page_source
soup_page = BeautifulSoup(soup_file, "html.parser")

main_table = soup_page.find_all('td', {'class': 'name table-participant'})

write_header()

for event in main_table:
    try:
        url_event = URL_BASE + event.find('a')['href']
        wd.get(url_event)
        soup_file = wd.page_source
        soup_page = BeautifulSoup(soup_file, "html.parser")
        
        main_table = soup_page.find('table', {'class': 'table-main detail-odds sortable'})
        table_rows = main_table.find_all('tr')
        odds_info = get_odds(table_rows, True)
        media_home, media_away = median_of_odds_twoway(odds_info)
        
        write_odds(media_home*100,media_away*100)
        #print("Home win probability: {:.2f}%".format(media_home*100))
        #print("Away win probability: {:.2f}%".format(media_away*100))
        
        result = (soup_page.find('p', {'class': 'result'})).find('strong').text
        write_score(result)
        #print(f"Final Score: {result}")
    except:
        print('An error was encountered.')