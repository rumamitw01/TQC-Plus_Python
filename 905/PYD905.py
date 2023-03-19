data=[]
temp_string=""
f_name = input()
string = input()
f_r=open(f_name,"r")
print("=== Before the deletion")
print(f_r.read())
f_r=open(f_name,"r")
# TODO
for i in f_r.read():
    if i!=" " and i!="\n":
        temp_string+=i
    else:
        data.append(temp_string)
        temp_string=""
        data.append(i)
f_r.close()
# TODO
if data.index(string):
    data.remove(string)
f_w=open(f_name,"w")
f_w.writelines(data)
f_w.close()
print("=== After the deletion")
f_r=open(f_name,"r")
# TODO
print(f_r.read())
f_r.close()