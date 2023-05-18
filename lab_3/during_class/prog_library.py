import argparse
from Library_class import Library

parser = argparse.ArgumentParser(description='This is Library, be quiet.')
parser.add_argument('file', type=str, default="")

args = parser.parse_args()

if __name__ == '__main__':
    if args.file == "":
        print("File name not specified")
        raise EOFError
    library = Library(args.file)
    library.parseFileLine()
    try:
        while True:
            library.parseInputLine(input())
    except EOFError:
        print(library.myBooks)
        print(library.borrowedBooks)