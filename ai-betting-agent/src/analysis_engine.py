class AnalysisEngine:
    """Cervello statistico dell'agente."""
    def calculate(self, data):
        total = data['home_power'] + data['away_power']
        p1 = round(data['home_power'] / total, 2)
        p2 = round(data['away_power'] / total, 2)
        px = round(1.0 - p1 - p2, 2)
        return {"1": p1, "X": px, "2": p2}