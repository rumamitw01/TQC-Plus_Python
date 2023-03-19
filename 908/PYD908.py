data=[]
data_count=[]
temp_string=""
f_name = input()
n = int(input())
with open(f_name,"r") as file:
    for i in file.read():
        if i!=" " and i!="\n":
            temp_string+=i
        else:
            data.append(temp_string)
            temp_string=""
            data.append(i)
    data.append(temp_string)
# TODO
data_set=sorted(set(data))
for i in data_set:
    data_count.append(data.count(i))
data=list(data_set)
for i in range(len(data_count)):
    if data_count[i]==n:
        print(data[i])