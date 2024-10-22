# import filecmp
# import pytest
# import os
# def read_file(file_path):
#     """Lit le contenu d'un fichier et renvoie une liste de lignes."""
#     with open(file_path, 'r') as f:
#         return f.readlines()
# @pytest.fixture(scope='module')
# def files():
#     """Renvoie les chemins des fichiers à tester."""
#     file1 = os.environ.get('RO')
#     file2 = os.environ.get('RP')
#     return file1, file2
# def test_file_comparison(files):
#     """Compare le contenu de file1 et file2."""
#     file1, file2 = files
#     # Vérifiez que les fichiers existent avant de les lire
#     assert os.path.exists(file1), f"Le fichier {file1} n'existe pas."
#     assert os.path.exists(file2), f"Le fichier {file2} n'existe pas."
#     # Lire le contenu des fichiers
#     # content_file1 = read_file(file1)
#     # content_file2 = read_file(file2)
#     # Vérifier que le contenu des fichiers est identique
#     # assert content_file1 == content_file2, f"Les fichiers {file1} et {file2} sont différents."
    
#     # shallow comparison
#     result = filecmp.cmp(file1, file2)
#     assert result

import filecmp
import pytest
import os

def read_file(file_path):
    """Lit le contenu d'un fichier et renvoie une liste de lignes."""
    with open(file_path, 'r') as f:
        return f.readlines()

@pytest.fixture(scope='module')
def files():
    """Renvoie les chemins des fichiers à tester."""
    file1 = os.environ.get('RO')  # Assurez-vous que cette variable d'environnement est définie
    file2 = os.environ.get('RP')  # Assurez-vous que cette variable d'environnement est définie
    assert file1 is not None, "Le chemin du fichier 1 n'est pas défini."
    assert file2 is not None, "Le chemin du fichier 2 n'est pas défini."
    return file1, file2

def test_file_comparison(files):
    """Compare le contenu de file1 et file2."""
    file1, file2 = files
    
    # Vérifiez que les fichiers existent avant de les lire
    assert os.path.exists(file1), f"Le fichier {file1} n'existe pas."
    assert os.path.exists(file2), f"Le fichier {file2} n'existe pas."

    # Comparaison superficielle
    result = filecmp.cmp(file1, file2)
    assert result, f"Les fichiers {file1} et {file2} sont différents."
