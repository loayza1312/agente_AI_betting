from src.analysis_engine import AnalysisEngine

def test_analysis():
    ae = AnalysisEngine()
    result = ae.analyze({
        "form_score_home": 3,
        "form_score_away": 4,
        "home_goals_avg": 1.5,
        "away_goals_avg": 1.8
    })
    assert result["home_strength"] > 0
