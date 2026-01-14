from src.data_collector import DataCollector

def test_data_collector():
    dc = DataCollector()
    data = dc.collect_match_data("Milan", "Inter")
    assert "odds" in data
