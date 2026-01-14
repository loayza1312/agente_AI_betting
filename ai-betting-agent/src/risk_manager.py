class RiskManager:
    def evaluate(self, analysis):
        diff = abs(analysis["home_strength"] - analysis["away_strength"])

        if diff < 0.5:
            return "HIGH RISK"
        elif diff < 1.5:
            return "MEDIUM RISK"
        else:
            return "LOW RISK"
