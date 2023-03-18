# TODO
temp_string=input()
temp_list=[i for i in temp_string]
temp_list[0]=temp_list[0].upper()
for i in range(len(temp_list)):
    if temp_list[i-1]==" ":
        temp_list[i]=temp_list[i].upper()
print(temp_string.upper())
for i in temp_list:
    print(i,end="")