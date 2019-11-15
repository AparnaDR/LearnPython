import utils
from pathlib import Path

"""
max = utils.find_max([11,3,4,5,666])
print(max)

"""

path = Path("ecommerce")
print(path.exists())

path = Path("taxes")
print(path.mkdir())

path = Path("taxes")
print(path.rmdir())

# to get all files in your current directory
path = Path()
for file in path.glob('*.py'): # we can search for any extension or any pattern
    print(file)
