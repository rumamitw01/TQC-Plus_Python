# TODO
def fib(x):
    temp=[0,1]
    for i in range(2,x):
        temp.append(temp[i-2]+temp[i-1])
    return temp
a=eval(input())
for i in fib(a):
    print(i,end=" ")