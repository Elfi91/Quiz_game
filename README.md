# Progetto: Quizzettone Python 🧠

Questo progetto implementa un semplice gioco a quiz (CLI - Command Line Interface) in Python. L'obiettivo principale è stato il **Refactoring** del codice per riorganizzarlo in **package** logici (`data` e `ui`), migliorando così la modularità e la manutenibilità del progetto.

---

## 📁 Struttura del Package

La struttura del codice è organizzata nei seguenti package logici all'interno della cartella radice `QUIZ_GAME/`:

* **`main.py`**: Il punto d'ingresso e il cuore della logica di esecuzione del quiz (ciclo `while`, gestione della navigazione e calcolo finale delle statistiche).
* **`data/`**: Contiene la logica per l'accesso e la manipolazione dei dati.
    * `repository.py`: **Repository Layer**. Interfaccia di basso livello per l'I/O (apertura e lettura dei file di testo).
    * `services.py`: **Service Layer**. Logica di business per trasformare i dati grezzi in modelli utilizzabili (ottenere la lista domande, estrarre il contenuto domanda/risposta).
* **`ui/`**: Contiene la logica di interfaccia utente.
    * `console.py`: Funzioni dedicate alla visualizzazione delle domande, del feedback e dello stato del quiz (output a console).
* **`domande_risposte/`**: Cartella contenente i file di testo delle risorse (il file indice e le singole domande/risposte).

---

## 🚀 Requisiti

Per eseguire questo progetto, è necessario **Python 3.x**.

---

## 🚩 Stato e Obiettivi

### Stato Attuale

La **struttura dei package** (`data/`, `ui/`, `domande_risposte/`) è stata **creata** correttamente nella cartella radice `QUIZ_GAME/`.

### Prossimi Passi

1.  **Copia del Codice Funzionale:** Inserire il codice Python nei moduli (`repository.py`, `services.py`, `console.py`).
2.  **Correzione degli Import Interni:** Aggiornare l'importazione in `data/services.py` (da relativo a `repository`).
3.  **Correzione degli Import di Alto Livello:** Aggiornare tutti gli import in `main.py` per puntare correttamente ai nuovi package (`data.services` e `ui.console`).
4.  **Correzione dei Percorsi:** Aggiornare le stringhe dei percorsi nel codice per riflettere la nuova posizione della cartella `domande_risposte/`.