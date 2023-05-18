import argparse
from DoSth_class import *

parser = argparse.ArgumentParser(description='This is Library, be quiet.')
parser.add_argument('login', type=str, default="")

args = parser.parse_args()

if __name__ == '__main__':
    login = args.login
    print(f"Try: {login}")
    doWhenAdmin(login)
    doWhenUser(login)
