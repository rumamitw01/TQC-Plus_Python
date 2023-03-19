data=[]
file = open("write.txt","w")
# TODO
for i in range(4):
    data.append(input()+"\n")
data.append(input())
file.writelines(data)
file.close()