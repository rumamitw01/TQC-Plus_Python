# TODO
row=eval(input())
for i in range(row):
    for j in range(row-i,1,-1):
        print(" ",end="")
    for k in range(0,i*2+1):
        print("*",end="")
    print()