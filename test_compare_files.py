import pytest
import filecmp
import sys

@pytest.mark.parametrize("file1, file2", [(sys.argv[1], sys.argv[2])])
def test_compare_files(file1, file2):
    """Compare two files and assert that they are identical."""
    assert filecmp.cmp(file1, file2, shallow=False), f"{file1} and {file2} are different."
