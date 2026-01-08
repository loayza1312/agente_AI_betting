class ReportModule:
    """Trasforma i dati in un report leggibile (Output)."""
    def generate(self, name, probs, decisions):
        text = f"### 📊 Report Analisi: {name}\n"
        text += f"**Probabilità calcolate dall'IA:** Casa: {probs['1']} | Pareggio: {probs['X']} | Ospiti: {probs['2']}\n\n"
        for res, data in decisions.items():
            status = "✅ CONSIGLIATO" if data['is_value'] else "❌ NON CONVIENE"
            text += f"- **Esito {res}**: {status} (Stake: {data['stake']}€)\n"
        text += "\n*Nota: Analisi basata su modelli probabilistici.*"
        return text