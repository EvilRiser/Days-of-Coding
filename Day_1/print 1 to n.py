import sys
from typing import List, Optional

sys.stdout = open("./output.txt", "w")
sys.stdin = open("./input.txt", "r")

my_output = []


def print_nos(x: int) -> Optional[List[int]]:
    if x < 1:
        return
    print_nos(x - 1)
    my_output.append(x)
    return my_output


if __name__ == '__main__':
    input_ = int(input())
    print(*print_nos(input_))
