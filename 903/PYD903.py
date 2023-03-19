data=[]
file = open("data.txt","a")
# TODO
data.append("\n")
for i in range(4):
    data.append(input()+"\n")
data.append(input())
file.writelines(data)
file.close()
print("Append completed!")
print('Content of "data.txt":')
# TODO
file2 = open("data.txt","r")
print(file2.read())