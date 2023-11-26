import sys
sys.stdout = open("./output.txt","w")
sys.stdin = open("./input.txt","r")


from typing import List


my_output = []


def printNos(x: int) -> List[int]:
    # Write your code here
    if x < 1:
        return
    else:
        printNos(x-1)
        my_output.append(x)
    return my_output


if __name__ == '__main__':
    x = int(input())
    printNos(x)
