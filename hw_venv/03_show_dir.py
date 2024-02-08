from colorama import Fore, Back, Style
import numpy
from pathlib import Path

directory = Path("hw_venv")

for path in directory.iterdir():
    if Path.is_dir(path):
        print(Fore.RED, f"|-{path}")
    else:
        print(Fore.GREEN, f"   -{path}")

