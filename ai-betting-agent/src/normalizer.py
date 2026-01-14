class DataNormalizer:
    def normalize(self, raw_data):
        return {
            "teams": f"{raw_data['home_team']} vs {raw_data['away_team']}",
            "form_score_home": sum(raw_data["home_form"]),
            "form_score_away": sum(raw_data["away_form"]),
            "home_goals_avg": raw_data["home_goals_avg"],
            "away_goals_avg": raw_data["away_goals_avg"],
            "odds": raw_data["odds"]
        }
