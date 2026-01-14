try:
    from langchain_groq import ChatGroq
except Exception:
    ChatGroq = None

class ReasoningModule:
    def __init__(self):
        self.llm = None
        if ChatGroq is not None:
            try:
                self.llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0.2)
            except Exception:
                # LLM not configured (missing API key or network); fallback to None
                self.llm = None

    def generate_reasoning(self, match, analysis, odds):
        prompt = f"""
You are an AI betting analyst.
Match: {match}

Stats:
Home strength: {analysis['home_strength']}
Away strength: {analysis['away_strength']}
Odds: {odds}

Produce a logical betting prediction with explanation.
"""
        if self.llm is None:
            # fallback rule-based explanation
            prediction = "home" if analysis["home_strength"] > analysis["away_strength"] else "away"
            return {
                "prediction": prediction,
                "reason": f"home_strength={analysis['home_strength']}, away_strength={analysis['away_strength']}",
                "note": "fallback (LLM unavailable)"
            }

        # when LLM is available, return its content
        return self.llm.invoke(prompt).content
