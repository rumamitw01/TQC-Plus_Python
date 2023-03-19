data=[]
sex=[]
temp_string=""
f_name = "read.dat"
# TODO
file=open(f_name,"r",encoding="utf-8")
for i in file.readlines():
    data.append(i)
for i in data:
    print(i)
for i in range(1,len(data)):
    sex.append(data[i][8])
male=sex.count("1")
female=sex.count("0")
print(f"Number of males: {male}")
print(f"Number of females: {female}")