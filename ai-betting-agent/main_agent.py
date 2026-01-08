from src.data_collector import DataCollector
from src.normalizer import DataNormalizer
from src.analysis_engine import AnalysisEngine
from src.reasoning_module import ReasoningModule
from src.risk_manager import RiskManager
from src.report_module import ReportModule

class BettingAgent:
    """Entry point dell'agente intelligente (Capitolo 6)."""
    def __init__(self):
        self.collector = DataCollector()
        self.normalizer = DataNormalizer()
        self.analyzer = AnalysisEngine()
        self.reasoner = ReasoningModule()
        self.risk = RiskManager()
        self.reporter = ReportModule()

    def analyze_match(self, match_id, bankroll):
        # 1. OSSERVAZIONE: Recupero dati grezzi
        raw_data = self.collector.fetch(match_id)
        if not raw_data: return "Match non trovato."

        # 2. PRE-ELABORAZIONE: Pulizia dati
        clean_data = self.normalizer.process(raw_data)

        # 3. RAGIONAMENTO: Calcolo probabilità (Intelligence)
        probabilities = self.analyzer.calculate(clean_data)

        # 4. DECISIONE: Identificazione valore
        value_analysis = self.reasoner.evaluate(probabilities, clean_data['odds'])

        # 5. GESTIONE RISCHIO: Calcolo stake (Constraints)
        final_decisions = self.risk.apply_limits(value_analysis, bankroll)

        # 6. AZIONE: Generazione Report
        return self.reporter.generate(clean_data['teams'], probabilities, final_decisions)