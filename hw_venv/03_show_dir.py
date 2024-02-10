from colorama import Fore, Back, Style
import numpy
from pathlib import Path

# directory = Path("hw_venv")

def read_path(folder, space = 0):
    directory = Path(folder)
    for path in directory.iterdir():
        if Path.is_dir(path):
            print(Fore.RED, f"{" "*space}|-{path}")
            read_path(path, space = space +1)

        else:
            print(Fore.GREEN, f"{" "*space}-{path}")
        

if __name__ == "__main__":
    read_path("hw_venv\\Scripts")