class AnalysisEngine:
    def analyze(self, data):
        home_strength = data["form_score_home"] + data["home_goals_avg"]
        away_strength = data["form_score_away"] + data["away_goals_avg"]

        return {
            "home_strength": round(home_strength, 2),
            "away_strength": round(away_strength, 2)
        }
