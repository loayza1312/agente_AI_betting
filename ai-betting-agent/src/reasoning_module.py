class ReasoningModule:
    """Confronta probabilità dell'agente vs quote del mercato."""
    def evaluate(self, probs, odds):
        results = {}
        for res, prob in probs.items():
            odd = odds[res]
            ev = prob * odd # Valore atteso
            results[res] = {"is_value": ev > 1.05, "expected_value": round(ev, 2)}
        return results