import sys
sys.stdout = open("./output.txt", "w")
sys.stdin = open("./input.txt", "r")

my_str = "Coding Ninjas"


def printNTimes(n: int) -> None:
    if n < 1:
        return
    printNTimes(n-1)
    print(my_str, end=" ")


if __name__ == '__main__':
    # input_=4
    input_ = int(input())
    printNTimes(input_)
