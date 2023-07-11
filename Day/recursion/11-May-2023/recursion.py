import sys

sys.stdout = open("../output.txt","w")
sys.stdin = open("../input.txt","r")

''''
Pre-requisite
 * function
 * coding
'''

'''
Recursion: When a function calls itself 
until a specified condition is met.

void f(){
    print(1)
    f()
}
main(){
    f()
}

'''

def print_number():
    print(1)
    print_number()


count=0
def print_cnt_number():
    global count
    if count == 11: # base condition
        return
    print(count)
    count += 1
    print_cnt_number()


if __name__=="__main__":
    # print_number() # --> infinite loop since no exit condition
    print_cnt_number()


