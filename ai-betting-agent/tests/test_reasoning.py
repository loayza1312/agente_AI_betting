from src.reasoning_module import ReasoningModule

def test_reasoning_output():
    rm = ReasoningModule()
    out = rm.generate_reasoning("Milan vs Inter",
                                {"home_strength": 4.2, "away_strength": 5.1},
                                {"home": 2.4, "draw": 3.2, "away": 2.7})
    assert isinstance(out, str)
