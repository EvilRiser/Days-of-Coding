import sys
sys.stdout = open("./output.txt","w")
sys.stdin = open("./input.txt","r")

my_str = "Coding Ninjas"


def printNtimes(n: int) -> None:
    if n<1:
        return
    printNtimes(n-1)
    print(my_str, end=" ")


if __name__ == '__main__':
    # n=4
    n = int(input())
    printNtimes(n)
