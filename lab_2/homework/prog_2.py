import re

# PROGRAM TAKES AS INPUT A WHOLE SENTENCE AND IS CHECKING EVERY WORD

def print_output(future_word):
    if future_word.isdigit() and future_word != "":
        print("Liczba:", future_word)
    elif future_word != "":
        print("Wyraz:", future_word)
    future_word = ""
    return future_word


def match_case(case, future_word):
    if re.match("[a-zA-Ząę]", case):
        if future_word.isdigit():
            future_word = print_output(future_word)
    elif re.match("[0-9]", case):
        if not future_word.isdigit():
            future_word = print_output(future_word)
    future_word = future_word + case
    return future_word


def cover_one_item(item):
    future_word = ""
    for position in item:
        future_word = match_case(position, future_word)
    print_output(future_word)


if __name__ == "__main__":
    arr = input().split()
    for item in arr:
        cover_one_item(item)
