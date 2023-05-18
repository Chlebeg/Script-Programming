import argparse
import re

parser = argparse.ArgumentParser(description='Conversion of logical lines to physical.')
parser.add_argument('-c', type=str, help="A continuation character for input files (default: '\\n')")
parser.add_argument('--leading_spaces', action="store_true", help="Deletes all of leading spaces")
parser.add_argument('--spaces', action="store_true", help="Deletes all spaces, without leading ones")
parser.add_argument('file', type=str, nargs='*', default="")

args = parser.parse_args()

# Examples:
# .\prog_4.py file.py
# output: "file.py:
#               a=      1      +  2*3            -4
# print(a)"
####################################################
# .\prog_4.py file.txt --leading_spaces
# output: "file.py:
# a=      1      +  2*3-4
# print(a)"
####################################################
# .\prog_4.py file.txt --spaces
# output: "file.py:
#              a=1+2*3            -4
# print(a)"
####################################################
# .\prog_4.py file.txt --spaces  --leading_spaces
# output: "file.py:
# a=1+2*3-4
# print(a)"


def normal_mode(line, cont_char):
    result = (line.split(cont_char))[0]
    return result


def leading_spaces_mode(line):
    return (re.findall(r"[^\s].*", line, re.DOTALL))[0]


def spaces_mode(line):
    result = ""
    first_char_flag = False
    for i in line:
        if not first_char_flag and i != " ":
            first_char_flag = True
        elif not first_char_flag:
            result = result + i
        if first_char_flag and i != " ":
            result = result + i
    return result


def do_operations_on_line(line, cont_char):
    line = normal_mode(line, cont_char)
    if args.leading_spaces:
        line = leading_spaces_mode(line)
    if args.spaces:
        line = spaces_mode(line)
    return line


def do_operations_on_data(file_data):
    if args.c:
        cont_char = args.c
    else:
        cont_char = '\\'
    i = 0
    for line in file_data:
        line = do_operations_on_line(line, cont_char)
        file_data[i] = line
        i += 1
    return "".join(file_data)


if __name__ == '__main__':
    if args.file == "":
        print("Specify file name")
        args.file = (input()).split()
    for file_name in args.file:
        file = open(file_name, "r")
        file_data = file.readlines()
        file.close()
        print("{}:\n{}".format(file_name, do_operations_on_data(file_data)))
