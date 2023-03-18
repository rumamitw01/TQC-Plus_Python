# TODO
a=eval(input())
b=eval(input())
total=0
temp=0
if a%2==1:
    temp=a+1
else:
    temp=a
while temp<=b:
    total+=temp
    temp+=2
print(total)