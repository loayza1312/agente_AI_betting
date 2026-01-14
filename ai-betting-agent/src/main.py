from flask import Flask, request, jsonify
from data_collector import DataCollector
from normalizer import DataNormalizer
from analysis_engine import AnalysisEngine
from reasoning_module import ReasoningModule
from risk_manager import RiskManager
from report_module import ReportModule

app = Flask(__name__)

collector = DataCollector()
normalizer = DataNormalizer()
analysis_engine = AnalysisEngine()
reasoner = ReasoningModule()
risk_manager = RiskManager()
reporter = ReportModule()

@app.route("/analyze", methods=["POST"])
def analyze():
    payload = request.get_json(silent=True) or {}
    # use provided data or fallback to collector mock
    data = payload.get("data") if payload.get("data") else collector.collect_match_data(None, None)

    normalized = normalizer.normalize(data)
    analysis = analysis_engine.analyze(normalized)

    try:
        reasoning = reasoner.generate_reasoning(normalized.get("teams"), analysis, normalized.get("odds"))
    except Exception as e:
        # fallback simple reasoning if LLM unavailable
        reasoning = {
            "prediction": "home" if analysis["home_strength"] > analysis["away_strength"] else "away",
            "note": "fallback reasoning used",
            "error": str(e)
        }

    risk = risk_manager.evaluate(analysis)
    report = reporter.generate(reasoning, risk)

    return jsonify(report)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
