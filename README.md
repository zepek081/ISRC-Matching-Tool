Guida all'utilizzo degli script ISRCMATCH.py e ISRCMATCH2.py

Questi due script Python sono utilizzati per confrontare e associare i codici ISRC tra due file Excel provenienti da DJ Monitor e SoundMouse. Di seguito sono descritti i passaggi per utilizzare questi script.

## Prerequisiti

Assicurati di avere installato Python e la libreria **pandas**. Puoi installarla utilizzando pip:

```bash
pip install pandas
```


## Descrizione degli Script

### 1. **ISRCMATCH.py**

Questo script carica due file Excel contenenti codici ISRC: uno da DJ Monitor e uno da SoundMouse. Lo scopo di questo script è di trovare i codici ISRC che corrispondono tra i due file e generare un nuovo file con i risultati.

#### Come usare ISRCMATCH.py

1.  **Modifica i percorsi dei file:**
    
    -   Modifica le variabili `file_dj_monitor`, `file_soundmouse` e `output_file` per riflettere i percorsi corretti dei tuoi file Excel.
    
    Esempio:
    
    python
    
    CopiaModifica
    
    `file_dj_monitor = r"C:\Users\user\Desktop\ISRC MATCH\DJ Monitor GEN 25 LCE.xlsx"
    file_soundmouse = r"C:\Users\user\Desktop\ISRC MATCH\SoundMouse LCE.xlsx"
    output_file = r"C:\Users\user\Desktop\ISRC MATCH\ISRC_MATCH_OUTPUT.xlsx"` 
    
2.  **Esegui lo script:** Una volta configurati i file, esegui lo script per trovare i codici ISRC corrispondenti tra i due file.
    
    bash
    
    CopiaModifica
    
    `python ISRCMATCH.py` 
    
3.  **Risultato:** Se ci sono dei match, verrà generato un file chiamato `ISRC_MATCH_OUTPUT.xlsx` contenente tutte le righe che corrispondono. Se non vengono trovati match, lo script ti informerà con il messaggio "Nessun match trovato."
    

----------

### 2. **ISRCMATCH2.py**

Questo script prende il file generato da **ISRCMATCH.py** (`ISRC_MATCH_OUTPUT.xlsx`) e il file originale di DJ Monitor (`DJ Monitor GEN 25 LCE.xlsx`), e mappa i codici ISRC con i nomi dei file audio corrispondenti. Aggiunge una colonna "AUDIO FILE NAME" al file di output.

#### Come usare ISRCMATCH2.py

1.  **Modifica i percorsi dei file:**
    
    -   Modifica le variabili `file_isrc_match_output` e `file_dj_monitor` per riflettere i percorsi corretti dei tuoi file Excel.
    
    Esempio:
    
    python
    
    CopiaModifica
    
    `file_isrc_match_output = r"C:\Users\user\Desktop\ISRC MATCH\ISRC_MATCH_OUTPUT.xlsx"
    file_dj_monitor = r"C:\Users\user\Desktop\ISRC MATCH\DJ Monitor GEN 25 LCE.xlsx"` 
    
2.  **Esegui lo script:** Una volta configurati i file, esegui lo script per aggiornare il file con la nuova colonna "AUDIO FILE NAME".
    
    bash
    
    CopiaModifica
    
    `python ISRCMATCH2.py` 
    
3.  **Risultato:** Lo script aggiornerà il file `ISRC_MATCH_OUTPUT.xlsx` e creerà un nuovo file chiamato `ISRC_MATCH_OUTPUT_UPDATED.xlsx` con la colonna aggiunta.
    

----------

## Errori Comuni

-   **Colonna ISRC mancante:** Se una delle colonne ISRC non è presente in uno dei file, lo script restituirà un errore. Verifica che la colonna ISRC sia correttamente nominata e contenuta nei file.
-   **Problemi con i dati:** Se ci sono celle vuote o formati di dati non validi, gli script rimuoveranno automaticamente le righe problematiche.

----------

## Conclusioni

Questi script ti consentono di confrontare facilmente i codici ISRC tra due file Excel e aggiungere informazioni extra sui file audio. Assicurati di avere i file correttamente formattati e i percorsi impostati prima di eseguire gli script.

vbnet

CopiaModifica

 ``Puoi copiare e incollare l'intero blocco sopra direttamente nel tuo file `.md`.``
