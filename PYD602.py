# TODO
temp_list=[]
for i in range(5):
    temp=input()
    if temp=="J":
        temp_list.append(11)
    elif temp=="Q":
        temp_list.append(12)
    elif temp=="K":
        temp_list.append(13)
    elif temp=="A":
        temp_list.append(1)
    else:
        temp_list.append(eval(temp))
total=0
for i in temp_list:
    total+=i
print(total)