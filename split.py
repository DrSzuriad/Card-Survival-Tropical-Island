import pandas as pd
import os

def split_csv(input_file, output_file):
    # Wczytanie pliku CSV
    df = pd.read_csv(input_file, encoding="utf-8-sig", header=None)
    
    # Poprawa nagłówków, jeśli pierwsza kolumna zawiera błędny nagłówek
    df.columns = ["KEY", "COLUMN_2", "COLUMN_3"]
    
    df_1 = df[["KEY", "COLUMN_2"]]
    df_1.to_csv(output_file, header=False, index=False, encoding="utf-8")
    print(f"Plik 1 został zapisany jako: {output_file}")
    
#    df_2 = df[["KEY", "COLUMN_3"]]
#    df_2.to_csv("files/pl/Pl.csv", header=False, index=False, encoding="utf-8")
#    print(f"Plik 2 został zapisany jako:")

# Przykładowe użycie
input_file = "game/Pl.csv"
output_file = "files/en/Pl.csv"
split_csv(input_file, output_file)