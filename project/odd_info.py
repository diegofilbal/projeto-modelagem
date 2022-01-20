class OddInfo:
    def __init__(self, home_odd, draw_odd, away_odd, bookmaker, payout):
        self.home_odd = home_odd
        self.draw_odd = draw_odd
        self.away_odd = away_odd
        self.bookmaker = bookmaker
        self.payout = payout


class OddInfoTwoWay:
    def __init__(self, home_odd, away_odd, bookmaker, payout):
        self.home_odd = home_odd
        self.away_odd = away_odd
        self.bookmaker = bookmaker
        self.payout = payout