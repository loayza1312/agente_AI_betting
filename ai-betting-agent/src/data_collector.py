import requests

class DataCollector:
    def __init__(self):
        self.mock_data = {
            "home_team": "Milan",
            "away_team": "Inter",
            "home_form": [1, 1, 0, 1, 0],
            "away_form": [1, 1, 1, 0, 1],
            "home_goals_avg": 1.6,
            "away_goals_avg": 1.9,
            "odds": {
                "home": 2.40,
                "draw": 3.20,
                "away": 2.70
            }
        }

    def collect_match_data(self, home, away):
        # In produzione: API-Football / OddsAPI
        return self.mock_data
