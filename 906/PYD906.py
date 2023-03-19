data=[]
temp_string=""
f_name = input()
str_old = input()
str_new = input()
#TODO
with open(f_name,"r") as file:
    for i in file.read():
        if i!=" " and i!="\n":
            temp_string+=i
        else:
            data.append(temp_string)
            temp_string=""
            data.append(i)
    data.append(temp_string)
for i in range(len(data)):
    if data[i]==str_old:
        data[i]=str_new
print("=== Before the replacement")
#TODO
with open(f_name,"r") as file:
    print(file.read())
print("=== After the replacement")
#TODO
with open(f_name,"w") as file2:
    file2.writelines(data)
with open(f_name,"r") as file:
    print(file.read())