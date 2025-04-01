import pandas as pd
import os

def split_csv(input_file, output_file_1, output_file_2):
    # Wczytanie pliku CSV
    df = pd.read_csv(input_file, encoding="utf-8")
    
    # Poprawa nagłówków, jeśli pierwsza kolumna zawiera błędny nagłówek
    df.columns = ["KEY", "COLUMN_2", "COLUMN_3"]
    
    # Tworzenie folderów, jeśli nie istnieją
    os.makedirs('en', exist_ok=True)
    os.makedirs('pl', exist_ok=True)
    
    # Tworzymy pierwszy plik w folderze "pl", który zawiera pierwszą i drugą kolumnę
    df_1 = df[["KEY", "COLUMN_2"]]
    df_1.to_csv(output_file_1, index=False, encoding="utf-8")
    print(f"Plik 1 został zapisany jako: {output_file_1}")
    
    # Tworzymy drugi plik w folderze "en", który zawiera pierwszą i trzecią kolumnę
    df_2 = df[["KEY", "COLUMN_3"]]
    df_2.to_csv(output_file_2, index=False, encoding="utf-8")
    print(f"Plik 2 został zapisany jako: {output_file_2}")

# Przykładowe użycie
input_path = "Pl.csv"
output_path_1 = "en/Pl.csv"
output_path_2 = "pl/Pl.csv"
split_csv(input_path, output_path_1, output_path_2)