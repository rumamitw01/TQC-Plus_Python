# TODO
temp=0
temp_set=set()
while temp!=-9999:
    temp=eval(input())
    if temp==-9999:
        break
    temp_set.add(temp)
print(f"Length: {len(temp_set)}")
print(f"Max: {max(temp_set)}")
print(f"Min: {min(temp_set)}")
print(f"Sum: {sum(temp_set)}")