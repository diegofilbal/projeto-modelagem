from odd_info import OddInfo
from odd import Odd


def get_bm_odd_info(table_line):
    try:
        divs_linha = table_line.find_all('div')
        payout_tag = table_line.find_all('span')
        tendency_tag = table_line.select('td[class*="right odds"]')

        bookmaker = ((str((divs_linha[0].find('a'))['title'])).split())[-2]
        payout = float(str(payout_tag[-1].text)[:-1])
        home_odd = Odd(float(tendency_tag[0].text), tendency_tag[0]['class'][-1])
        draw_odd = Odd(float(tendency_tag[1].text), tendency_tag[1]['class'][-1])
        away_odd = Odd(float(tendency_tag[2].text), tendency_tag[2]['class'][-1])

        info_odds = OddInfo(home_odd, draw_odd, away_odd, bookmaker,payout)
        return info_odds
    except:
        return None


def get_odds(odd_table):
    odd_list = []
    for table_row in odd_table:
        odd_info = get_bm_odd_info(table_row)
        if odd_info is not None:
            odd_list.append(odd_info)
    return odd_list
