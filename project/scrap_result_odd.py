from score_odd import ScoreOdd


def get_line_odd(line):
    odd = float((line.find('span', {'class':'avg nowrp'})).find('a').text)
    return odd

def get_line_score(line):
    score = (line.find('strong')).find('a').text
    return score

def get_line_info(line):
    try:
        odd = get_line_odd(line)
        score = get_line_score(line)
        return odd, score
    except:
        return None

def scrap_odds(page_cs):
    # avg nowrp table-header-light
    scores_lines = page_cs.select('div[class*="table-header-light"]')
    #print(scores_lines)
    odd, result = get_line_info(scores_lines[0])
    menor = ScoreOdd(odd, result)
    for line in scores_lines:
        data = get_line_info(line)
        if data is not None:
            line_data = ScoreOdd(data[0], data[1])
            if(line_data.value_odd < menor.value_odd):
                menor.value_odd = line_data.value_odd
                menor.score = line_data.score
    return menor
    