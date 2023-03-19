data=[]
temp_string=""
# TODO
f_name=input()
file=open(f_name,"r")
for i in file.read():
    if i!=" " and i!="\n":
        temp_string+=i
    else:
        data.append(temp_string)
        temp_string=""
        data.append(i)
l=data.count("\n")
w=data.count(" ")+data.count("\n")
file2=open(f_name,"r")
c=len(file2.read())-w
print(f"{l} line(s)")
print(f"{w} word(s)")
print(f"{c} character(s)")