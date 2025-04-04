import pandas as pd
import os

def split_csv(input_file, output_file_1, output_file_2):
    # Wczytanie pliku CSV
    df = pd.read_csv(input_file, encoding="utf-8")
    
    # Poprawa nagłówków, jeśli pierwsza kolumna zawiera błędny nagłówek
    df.columns = ["KEY", "COLUMN_2", "COLUMN_3"]
    
    # Tworzenie folderów, jeśli nie istnieją
    os.makedirs('en', exist_ok=True)
    
    df_1 = df[["KEY", "COLUMN_2"]]
    df_1.to_csv(output_file_1, header=False, index=False, encoding="utf-8")
    print(f"Plik 1 został zapisany jako: {output_file_1}")

# Przykładowe użycie
input_path = "game/Pl.csv"
output_path_1 = "files/en/Pl.csv"
output_path_2 = "files/pl/Pl.csv"
split_csv(input_path, output_path_1, output_path_2)