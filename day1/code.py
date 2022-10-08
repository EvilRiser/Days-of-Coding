import sys

sys.stdout = open("./output.txt","w")
sys.stdin = open("./input.txt","r")



### Arrays
l = [2200,2350,2600,2130,2190]

## Q1
extra = l[1]-l[0]
print("Extra:",extra)
## Q2

sum = 0 
for i in range(0,3):
    sum += l[i]

print("Total expense in First quarter:",sum)
## Q3
x = 2000
if x in l:
    print("Yes")
else:
    print("No")
## Q4
l.append(1980)
print(l)
## Q5
l[3] = l[3]-200
print(l)

