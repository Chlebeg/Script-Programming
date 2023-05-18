import argparse
from functionalClass.Bigger_library_class import Library

parser = argparse.ArgumentParser(description='This is Library, be quiet.')
parser.add_argument('bookDatabase', type=str, default="")
parser.add_argument('customerDatabase', type=str, default="")

args = parser.parse_args()

# bookDatabase: <A-buy/B-borrow>
# if buy: A <title> <author> <amount> <price>
# if borrow: B <title> <author>

# customerDatabase: <A-buyer/B-borrower>
# <name> <surname> <pesel>

if __name__ == '__main__':
    if args.bookDatabase == "" or args.customerDatabase == "":
        print("File name not specified")
        raise EOFError
    library = Library(args.bookDatabase, args.customerDatabase)
    library.parseBothDatabases()
    print("Now make request: [pesel] [+/-] [id]")
    try:
        while True:
            library.parseInputLine(input())
    except EOFError:
        print(library)
