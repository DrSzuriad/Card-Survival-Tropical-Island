import os
import shutil
import json

# Funkcja do wczytania zapisanej ścieżki z pliku konfiguracyjnego
def load_game_path():
    config_file = "game_path.json"
    
    if os.path.exists(config_file):
        with open(config_file, 'r') as file:
            config = json.load(file)
            return config.get('game_path')
    return None

# Funkcja do zapisania ścieżki gry do pliku konfiguracyjnego
def save_game_path(game_path):
    config_file = "game_path.json"
    config = {'game_path': game_path}
    
    with open(config_file, 'w') as file:
        json.dump(config, file)
    print(f"Ścieżka do folderu gry została zapisana: {game_path}")

# Funkcja do skopiowania pliku do stałego folderu wewnątrz gry
def copy_file_to_game_folder(file_to_copy):
    game_path = load_game_path()
    
    if not game_path:
        print("Nie znaleziono zapamiętanej ścieżki do folderu gry. Proszę podać ją ręcznie.")
        game_path = input("Podaj pełną ścieżkę do folderu gry: ")
        save_game_path(game_path)
    
    if os.path.exists(game_path):
        # Dodanie stałej ścieżki wewnątrz folderu gry (np. folder 'config')
        fixed_folder = os.path.join(game_path, "Card Survival - Tropical Island_Data/StreamingAssets/Localization")  # Zmieniamy "config" na dowolną nazwę folderu
        if not os.path.exists(fixed_folder):
            os.makedirs(fixed_folder)  # Tworzymy folder, jeśli nie istnieje
        
        destination_fixed_file = os.path.join(fixed_folder, os.path.basename(file_to_copy))
        try:
            shutil.copy(file_to_copy, destination_fixed_file)
            print(f"Plik '{file_to_copy}' został skopiowany do folderu '{fixed_folder}'.")
        except Exception as e:
            print(f"Wystąpił błąd podczas kopiowania pliku do folderu wewnątrz gry: {e}")
    else:
        print(f"Nie znaleziono folderu gry pod ścieżką: {game_path}")
# Przykład użycia:
file_to_copy = "mod/Pl.csv"  # Zmień na pełną ścieżkę do pliku, który chcesz skopiować
copy_file_to_game_folder(file_to_copy)