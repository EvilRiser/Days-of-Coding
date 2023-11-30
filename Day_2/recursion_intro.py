import sys

sys.stdout = open("./output.txt", "w")
sys.stdin = open("./input.txt", "r")


# RECURSION
'''
When a function calls itself,
until a specified condition is met
'''

count = 0


def print_number():
    global count
    if count == 7:
        return
    print(count, end=" ")
    count += 1
    print_number()


def print_reverse_number():
    global count
    count -= 1
    if count < 0:
        return
    print(count, end=" ")

    print_reverse_number()


if __name__ == '__main__':
    print_number()
    print()
    print_reverse_number()

    ''' Output
    0 1 2 3 4 5 6
    6 5 4 3 2 1 0
    '''