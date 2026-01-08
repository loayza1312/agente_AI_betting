class DataCollector:
    """Recupera i dati (Mock per uso gratuito)."""
    def fetch(self, match_id):
        db = {
            "Inter-Milan": {"home": 2.5, "away": 1.2, "odds": {"1": 1.90, "X": 3.40, "2": 4.50}},
            "Juve-Napoli": {"home": 1.5, "away": 1.5, "odds": {"1": 2.60, "X": 3.10, "2": 2.80}}
        }
        return db.get(match_id)