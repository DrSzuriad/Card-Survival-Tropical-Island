import pandas as pd
import os

def merge_csv(input_file_1, input_file_2, output_file):
    # Wczytanie plików CSV z folderów 'pl' i 'en'
    df_1 = pd.read_csv(input_file_1, header=None, names=["KEY", "COLUMN_2"])  # Wczytanie z nagłówkami "KEY" i "COLUMN_2"
    df_2 = pd.read_csv(input_file_2, header=None, names=["KEY", "COLUMN_3"])
    
    # Łączenie dwóch DataFrame'ów po kolumnie "KEY"
    df_merged = pd.merge(df_1, df_2, on="KEY", how="inner")  # Możesz zmienić 'how' na 'outer' w zależności od potrzeb
    
    # Sprawdzenie, czy w COLUMN_3 są puste wartości (NaN), i zastąpienie ich wartością z COLUMN_2
    df_merged['COLUMN_3'] = df_merged['COLUMN_3'].fillna(df_merged['COLUMN_2'])
    
    # Zapisanie połączonych danych do nowego pliku CSV
    df_merged.to_csv(output_file, index=False, encoding="utf-8")
    print(f"Plik został zapisany jako: {output_file}")

# Przykładowe użycie
input_path_1 = "files/en/Pl.csv" 
input_path_2 = "files/pl/Pl.csv"
output_path = "mod/Pl.csv"
merge_csv(input_path_1, input_path_2, output_path)