
import argparse
import os

def parse_args():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-t', '--test', default=False, action='store_true', help='run the unit tests')
    args = parser.parse_args()

    return args

def main():
    pass

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
