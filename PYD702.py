# TODO
print("Create tuple1:")
t1=0
temp_list=[]
while t1!=-9999:
    t1=eval(input())
    if t1==-9999:
        break
    temp_list.append(t1)
tuple_1=tuple(temp_list)
# TODO
print("Create tuple2:")
t2=0
temp_list=[]
while t2!=-9999:
    t2=eval(input())
    if t2==-9999:
        break
    temp_list.append(t2)
tuple_2=tuple(temp_list)
# TODO
temp_list=[]
for i in tuple_1:
    temp_list.append(i)
for i in tuple_2:
    temp_list.append(i)
final_tuple=tuple(temp_list)
sorted_list=sorted(temp_list)
print(f"Combined tuple before sorting: {final_tuple}")
print(f"Combined list after sorting: {sorted_list}")