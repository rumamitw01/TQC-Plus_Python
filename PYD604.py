# TODO
temp_list=[[],[]]
for i in range(10):
    temp_list[0].append(eval(input()))
for i in temp_list[0]:
   temp_list[1].append(temp_list[0].count(i))
for i in range(10):
    if temp_list[1][i]==max(temp_list[1]):
        print(temp_list[0][i])
        print(temp_list[1][i])
        break