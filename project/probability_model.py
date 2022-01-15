import numpy as np

def get_implied_probability(odd):
    implied_probability = 1/odd.value
    if odd.tendency == "up":
        implied_probability -= .05
    else:
        implied_probability += .05
    return implied_probability


def get_odd_weight(payout):
    return payout*payout

def probability_normalizer(home, draw, away):
    full_event = home + draw + away
    if full_event > 1:
        tax = (full_event - 1)/3
        home -= tax
        draw -= tax
        away -= tax
    else:
        tax = (1 - full_event)/3
        home += tax
        draw += tax
        away += tax
    return home, draw, away

def median_of_odds(odd_list):
    home_odds = []
    draw_odds = []
    away_odds = []
    odds_weight = []
    for odd in odd_list:
        wheight_bm = get_odd_weight(odd.payout)
        home_probability = get_implied_probability(odd.home_odd)
        draw_probability = get_implied_probability(odd.draw_odd)
        away_probability = get_implied_probability(odd.away_odd)

        odds_weight.append(wheight_bm)
        home_odds.append(home_probability)
        draw_odds.append(draw_probability)
        away_odds.append(away_probability)

    home_avg = np.average(home_odds, weights=odds_weight)
    draw_avg = np.average(draw_odds, weights=odds_weight)
    away_avg = np.average(away_odds, weights=odds_weight)
    
    home_avg, draw_avg, away_avg = probability_normalizer(home_avg,
                                                          draw_avg, away_avg)
    
    return home_avg, draw_avg, away_avg
