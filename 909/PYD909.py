f_name = "data.dat"
data=[]
file = open(f_name,"w")
for i in range(4):
    data.append(input())
    data.append("\n\n")
data.append(input())
data.append("\n")
file.writelines(data)
file.close()
# TODO
print('The content of "data.dat":')
file2=open(f_name,"r")
print(file2.read())