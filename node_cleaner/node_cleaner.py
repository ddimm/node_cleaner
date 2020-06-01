#!/usr/bin/env python3
import os
import sys
import argparse
import shutil
verbose = False




def clean_from_path(folder_path):
    try:
        os.chdir(folder_path)
    except FileNotFoundError as file_not_found:
        print(file_not_found, file=sys.stderr)
        sys.exit(1)
    for root, dirs, files in os.walk(folder_path, topdown=True):
        if "package.json" in files and "node_modules" in dirs:
            if verbose:
                print("cleaning package", root)
            try:
                shutil.rmtree(os.path.join(root, "node_modules"))
            except Exception as e:
                print(e, file=sys.stderr)
                continue
            

def main():
    global verbose
    parser = argparse.ArgumentParser()
    parser.add_argument('root', action='store',
                        help="root directory to search for node_modules. should be absolute path", type=str)
    parser.add_argument('-v', '--verbose',
                        help="set verbose output",  action="store_true")
    parser = parser.parse_args()
    root_folder = parser.root
    verbose = parser.verbose
    clean_from_path(root_folder)


if __name__ == "__main__":
    main()
