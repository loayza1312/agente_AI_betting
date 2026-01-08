import pytest
from src.data_collector import DataCollector
from src.analysis_engine import AnalysisEngine

def test_fetch_data():
    collector = DataCollector()
    assert collector.fetch_match_data("Inter-Milan") is not None
    assert collector.fetch_match_data("Inesistente") is None

def test_analysis_sum():
    engine = AnalysisEngine()
    dummy_data = {
        "home_stats": {"goals_scored": 10, "matches": 5, "form": 1},
        "away_stats": {"goals_scored": 10, "matches": 5, "form": 1}
    }
    probs = engine.calculate_probabilities(dummy_data)
    assert sum(probs.values()) == pytest.approx(1.0)