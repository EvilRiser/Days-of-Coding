import sys


sys.stdout = open("./output.txt", "w")
sys.stdin = open("./input.txt", "r")


def print_names_n_times(i, n):
    if i > n:
        return
    print(f"{i}. SS")
    print_names_n_times(i+1, n)


if __name__ == '__main__':
    n = int(input())
    print_names_n_times(1, n)
    '''Output
    1. SS
    2. SS
    3. SS
    4. SS
    5. SS
    
    TC = O(n)
    SC = O(n) --> stack space 
     -> f(1,3) 
     -> f(2,3)
     -> f(3,3) 
     -> f(4,3) - base condition
    '''
