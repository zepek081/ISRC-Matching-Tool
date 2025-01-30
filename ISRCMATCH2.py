import pandas as pd

# Percorsi dei file
file_isrc_match_output = r"C:\Users\user\Desktop\ISRC MATCH\ISRC_MATCH_OUTPUT.xlsx"
file_dj_monitor = r"C:\Users\user\Desktop\ISRC MATCH\DJ Monitor GEN 25 LCE.xlsx"

# Carica i dati
df_isrc_match = pd.read_excel(file_isrc_match_output)
df_dj_monitor = pd.read_excel(file_dj_monitor)

# Stampa i nomi delle colonne per diagnosticare l'errore
print("Colonne in ISRC_MATCH_OUTPUT.xlsx:", df_isrc_match.columns)
print("Colonne in DJ Monitor GEN 25 LCE.xlsx:", df_dj_monitor.columns)

# Verifica che la colonna ISRC sia presente
if 'ISRC' in df_isrc_match.columns and 'isrc' in df_dj_monitor.columns:
    # Crea un dizionario ISRC -> filename dal file DJ Monitor
    isrc_to_filename = pd.Series(df_dj_monitor['filename'].values, index=df_dj_monitor['isrc']).to_dict()

    # Mappa i valori della colonna ISRC in ISRC_MATCH_OUTPUT con i valori corrispondenti dalla colonna filename di DJ Monitor
    df_isrc_match['AUDIO FILE NAME'] = df_isrc_match['ISRC'].map(isrc_to_filename)

    # Salva il risultato in un nuovo file Excel
    df_isrc_match.to_excel(r"C:\Users\user\Desktop\ISRC MATCH\ISRC_MATCH_OUTPUT_UPDATED.xlsx", index=False)
    print("File aggiornato con successo.")
else:
    print("Le colonne 'ISRC' non sono presenti in uno dei file.")
