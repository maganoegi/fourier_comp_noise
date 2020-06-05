
import argparse
import os

import numpy as np 

from exercices import noise, compression

from fourier_lib import tfd, tfd2, tfdi, tfdi2

def parse_args():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-t', '--test', default=False, action='store_true', help='run the unit tests')
    parser.add_argument('-n', '--noise', default=False, action='store_true', help='noise exercice')
    parser.add_argument('-c', '--compression', type=int, help='fourier image compression exercice with as argument degree of compression : 0-9 : None to Max')
    return parser.parse_args()

def main():
    print("Please use the following flags:\n\
    \t-n\t\tNOISE EXERCICE\n\
    \t-c val[0-9]\tCOMPRESSION EXERCICE\n\
    \t-t\t\tUNIT TESTS FOR TFD TFDI TFD2 TFDI2\n\
    \nfor more info, please use --help")

def tests(filename):
    GREEN = "\033[92m"
    END = "\033[0m"
    print(f"\nexecuting tests in {GREEN}{filename}{END}\n")
    fileDir = os.path.dirname(os.path.abspath(__file__))
    os.system(f"python3 {fileDir}/tests.py")

if __name__ == "__main__":
    args = parse_args()

    if args.test:
        tests("tests.py")
    elif args.noise:
        noise()
    elif args.compression + 1:
        try:
            compression(args.compression)
        except AssertionError:
            print("ERROR: please give a degree of compression between 0 and 9")
    else:
        main()
