# test_compare_files.py
import pytest
import os

def read_file(file_path):
    """Lit le contenu d'un fichier et renvoie une liste de lignes."""
    with open(file_path, 'r') as f:
        return f.readlines()

def test_file_comparison():
    """Compare le contenu de file1 et file2."""
    # Obtenez les fichiers à partir des variables d'environnement
    file1 = os.environ.get('FILE1')
    file2 = os.environ.get('FILE2')

    # Vérifiez que les fichiers existent avant de les lire
    assert os.path.exists(file1), f"Le fichier {file1} n'existe pas."
    assert os.path.exists(file2), f"Le fichier {file2} n'existe pas."

    # Lire le contenu des fichiers
    content_file1 = read_file(file1)
    content_file2 = read_file(file2)

    # Vérifier que le contenu des fichiers est identique
    assert content_file1 == content_file2, f"Les fichiers {file1} et {file2} sont différents."
