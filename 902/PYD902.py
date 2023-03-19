f = open("read.txt","r")
# TODO
data=f.read().split()
f.close()
temp=0
for i in data:
    temp+=eval(i)
print(temp)