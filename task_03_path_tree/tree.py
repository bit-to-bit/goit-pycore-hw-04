'''Util for file system visualization'''

import sys
from pathlib import Path
from colorama import Fore, Style

GAP = "   "
ICO_DIR = "\U0001F4C1"
ICO_FILE = "\U0001F5CB"

def file_system_print(path: Path, level: int):
    '''Print file system tree'''

    for e in path.iterdir():
        if e.is_dir():
            print(GAP*level, ICO_DIR, Fore.WHITE  + e.name + Style.RESET_ALL)
            file_system_print(e, level+1)
        else:
            print(GAP*level, Fore.LIGHTBLACK_EX + ICO_FILE, e.name, Style.RESET_ALL)

def check_path() -> tuple:
    '''Checks if the specified path is correct'''

    is_folder, path = False, Path()
    args = sys.argv
    if len(args) != 2:
        print("The script requires one parameter")
    else:
        path = Path(args[1])
        if path.exists() and path.is_dir():
            is_folder = True
        else:
            print("The specified path is not a directory or does not exist")
    return (is_folder, path)

def main():
    '''App runtime'''
    is_folder, path = check_path()
    if is_folder:
        file_system_print(path, 0)

if __name__ == "__main__":
    main()
