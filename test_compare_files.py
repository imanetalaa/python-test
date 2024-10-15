# import pytest
# import filecmp
# import sys

# @pytest.mark.parametrize("file1, file2", [(sys.argv[1], sys.argv[2])])
# def test_compare_files(file1, file2):
#     """Compare two files and assert that they are identical."""
#     assert filecmp.cmp(file1, file2, shallow=False), f"{file1} and {file2} are different."



# conftest.py
def pytest_addoption(parser):
    parser.addoption("--file1", action="store", default="default1.txt", help="file1 help")
    parser.addoption("--file2", action="store", default="default2.txt", help="file2 help")

@pytest.fixture
def files(request):
    return request.config.getoption("--file1"), request.config.getoption("--file2")

