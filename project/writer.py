def write_header():
    try:
        results_file = open("result_season.csv", mode='w', encoding='utf-8')
        results_file.write('odd_home,odd_away,score_home,score_away\n')
        results_file.close()
    except:
        print("An error was encoutered while writing the header.")
        

def write_odds(odd_home,odd_away):
    try:
        results_file = open("result_season.csv", mode='a', encoding='utf-8')
        results_file.write("{:.2f}".format(odd_home))
        results_file.write(',')
        results_file.write("{:.2f}".format(odd_away))
        results_file.write(',')
        results_file.close()
    except:
        print("An error was encoutered while writing results.")

def split_score(result):
    only_result = result.split()[0]
    home_result, away_result = only_result.split(':')
    return home_result, away_result

def write_score(score):
    try:
        results_file = open("result_season.csv", mode='a', encoding='utf-8')
        home_result, away_result = split_score(score)
        results_file.write(home_result)
        results_file.write(',')
        results_file.write(away_result)
        results_file.write('\n')
        results_file.close()
    except:
        print("An error was encoutered while writing results.")