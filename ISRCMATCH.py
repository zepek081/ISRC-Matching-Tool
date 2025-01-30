import pandas as pd

# Percorsi dei file
file_dj_monitor = r"C:\Users\user\Desktop\ISRC MATCH\DJ Monitor GEN 25 LCE.xlsx"
file_soundmouse = r"C:\Users\user\Desktop\ISRC MATCH\SoundMouse LCE.xlsx"
output_file = r"C:\Users\user\Desktop\ISRC MATCH\ISRC_MATCH_OUTPUT.xlsx"

# Carica i file
df_dj_monitor = pd.read_excel(file_dj_monitor)
df_soundmouse = pd.read_excel(file_soundmouse)

# Seleziona la colonna ISRC da DJ Monitor (colonna I = indice 8)
df_dj_monitor_isrc = df_dj_monitor.iloc[:, 8]  # Colonna I è la nona (indice 8)
df_dj_monitor_isrc.columns = ['ISRC']  # Rinomina la colonna per chiarezza

# Verifica che la colonna ISRC sia presente in SoundMouse
if 'ISRC' in df_soundmouse.columns:
    # Normalizza gli ISRC (rimuove spazi extra e gestisce i NaN)
    df_soundmouse['ISRC'] = df_soundmouse['ISRC'].astype(str).str.strip()
else:
    print("Colonna 'ISRC' non trovata nel file SoundMouse.")
    exit(1)  # Esce se la colonna ISRC non esiste

# Rimuovi le righe con ISRC vuoti in entrambi i dataframe
df_dj_monitor_isrc = df_dj_monitor_isrc.dropna()
df_soundmouse = df_soundmouse.dropna(subset=['ISRC'])

# Filtro: seleziona tutte le righe di SoundMouse che corrispondono agli ISRC di DJ Monitor
df_matched = df_soundmouse[df_soundmouse['ISRC'].isin(df_dj_monitor_isrc)]

# Se ci sono dei match, salviamo il risultato con tutte le righe corrispondenti
if not df_matched.empty:
    df_matched.to_excel(output_file, index=False)
    print("File generato con successo:", output_file)
else:
    print("Nessun match trovato.")
