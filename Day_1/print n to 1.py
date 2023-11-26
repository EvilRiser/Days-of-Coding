import sys
sys.stdout = open("./output.txt","w")
sys.stdin = open("./input.txt","r")

from typing import List

my_output = []

def printNos(x:int) -> List[int]:
    if x < 1:
        return
    else:
        my_output.append(x)
        printNos(x-1)
        return my_output


if __name__ == '__main__':
    x = int(input())
    print(printNos(x))
