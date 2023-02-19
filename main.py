# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(next)

        if next in ")]}":
            prev = opening_brackets_stack.pop()
            if not are_matching(prev, next):
                return i+1
    return "Success"


def main():
    test = input()
    if 'I' == test[0]:
        text = input()
    mismatch = find_mismatch(text)
    print (mismatch)


if __name__ == "__main__":
    main()
