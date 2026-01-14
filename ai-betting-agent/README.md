# ai-betting-agent

Progetto demo: agent semplice per analisi scommesse con frontend statico.

## Struttura

- `src/` - logica core e `main.py` per eseguire la pipeline
- `web/` - frontend statico (demo)
- `tests/` - test con `pytest`

## Come usare

1. Installare dipendenze di test:

```bash
pip install -r requirements.txt
```

2. Eseguire la pipeline:

```bash
python src/main.py
```

3. Aprire il frontend demo:

Apri `web/index.html` in un browser (pagina statica con demo client-side).

## Note
File creati come punto di partenza: sostituisci gli stub con logiche reali (API, DB, modelli, gestione rischio avanzata, ecc.).
