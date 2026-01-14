class ReportModule:
    def generate(self, reasoning, risk):
        return {
            "analysis": reasoning,
            "risk_level": risk
        }
