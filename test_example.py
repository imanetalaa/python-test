# test_compare_files.py
import pytest

def read_file(file_path):
    """Lit le contenu d'un fichier et renvoie une liste de lignes."""
    with open(file_path, 'r') as f:
        return f.readlines()

def test_file_comparison(FILE1, FILE2):
    """Compare le contenu de file1 et file2."""
    # Lire le contenu des fichiers
    content_file1 = read_file(FILE1)
    content_file2 = read_file(FILE2)

    # Vérifier que le contenu des fichiers est identique
    assert content_file1 == content_file2, f"Les fichiers {FILE1} et {FILE2} sont différents."

# Note: Vous pouvez passer les paramètres FILE1 et FILE2 à pytest lors de l'exécution
