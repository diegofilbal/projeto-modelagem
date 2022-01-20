import sys

from get_predictions import print_outcomes, print_likely_score, get_final_score

#URL_EVENT = "https://www.oddsportal.com/basketball/usa/nba/los-angeles-lakers-indiana-pacers-rJbngKPj/#home-away;1"
URL_EVENT = str(sys.argv[1])

if __name__ == '__main__':
    if str(sys.argv[2]) == 'twoway':
        print_outcomes(True,URL_EVENT)
    else:
        print_outcomes(False,URL_EVENT)
        print_likely_score(URL_EVENT)
    if str(sys.argv[3] == 'past'):
        get_final_score(URL_EVENT)