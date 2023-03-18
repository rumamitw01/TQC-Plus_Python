# TODO
temp_list=[[],[],[]]
for i in range(3):
    for j in range(3):
        temp_list[i].append(eval(input()))
max_list=[max(temp_list[0]),max(temp_list[1]),max(temp_list[2])]
min_list=[min(temp_list[0]),min(temp_list[1]),min(temp_list[2])]
for i in range(3):
    for j in range(3):
        if temp_list[i][j]==max(max_list):
            print(f"Index of the largest number {max(max_list)} is: ({i}, {j})")
for i in range(3):
    for j in range(3):
        if temp_list[i][j]==min(min_list):
            print(f"Index of the smallest number {min(min_list)} is: ({i}, {j})")