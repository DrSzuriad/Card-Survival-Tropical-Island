import pandas as pd
import os

def merge_csv(input_file_1, input_file_2, output_file):
    # Wczytanie plików CSV z folderów 'pl' i 'en'
    df_1 = pd.read_csv(input_file_1, encoding="utf-8")
    df_2 = pd.read_csv(input_file_2, encoding="utf-8")
    
    # Łączenie dwóch DataFrame'ów po kolumnie "KEY"
    df_merged = pd.merge(df_1, df_2, on="KEY", how="inner")  # Możesz zmienić 'how' na 'outer' w zależności od potrzeb
    
    # Sprawdzenie, czy w COLUMN_3 są puste wartości (NaN), i zastąpienie ich wartością z COLUMN_2
    df_merged['COLUMN_3'] = df_merged['COLUMN_3'].fillna(df_merged['COLUMN_2'])
    
    # Zapisanie połączonych danych do nowego pliku CSV
    df_merged.to_csv(output_file, index=False, encoding="utf-8")
    print(f"Plik został zapisany jako: {output_file}")

# Przykładowe użycie
input_path_1 = "en/Pl.csv" 
input_path_2 = "pl/Pl.csv"
output_path = "Pl_merged.csv"
merge_csv(input_path_1, input_path_2, output_path)