class RiskManager:
    """Modulo di controllo: impedisce all'agente di rischiare troppo."""
    def apply_limits(self, analysis, bankroll):
        for res in analysis:
            if analysis[res]['is_value']:
                # Scommette massimo il 2% del budget se c'è valore
                analysis[res]['stake'] = round(bankroll * 0.02, 2)
            else:
                analysis[res]['stake'] = 0
        return analysis