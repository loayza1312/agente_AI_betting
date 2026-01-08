# AI Betting Agent

Questo progetto è un agente AI per l'analisi e il decision making nelle scommesse sportive. Utilizza moduli specializzati per raccogliere dati, analizzarli statisticamente, prendere decisioni logiche e gestire i rischi.

## Struttura del Progetto

- `src/data_collector.py`: Raccolta dei dati da fonti esterne.
- `src/normalizer.py`: Normalizzazione e pre-elaborazione dei dati.
- `src/analysis_engine.py`: Analisi statistica e generazione di insight.
- `src/reasoning_module.py`: Decision making logico.
- `src/risk_manager.py`: Gestione dei rischi e applicazione di vincoli.
- `src/report_module.py`: Generazione di report e output.
- `app.py`: Interfaccia grafica con Streamlit.
- `tests/test_modules.py`: Test automatici con Pytest.

## Installazione

1. Clona il repository.
2. Installa le dipendenze: `pip install -r requirements.txt`
3. Avvia l'app: `streamlit run app.py`

## Utilizzo

Avvia l'app e clicca su "Avvia Analisi" per simulare il processo di decision making.

## Test

Esegui i test con: `pytest tests/test_modules.py`

## Note

Questo è uno skeleton del progetto. Implementare la logica specifica per ciascun modulo in base alle esigenze.