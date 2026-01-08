class DataNormalizer:
    """Assicura che i dati siano nel formato corretto."""
    def process(self, raw):
        return {
            "teams": "Match Analizzato",
            "home_power": float(raw['home']),
            "away_power": float(raw['away']),
            "odds": raw['odds']
        }