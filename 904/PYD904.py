data = []
Height=[]
Weight=[]
temp_string=""
S_h=0
S_w=0
with open("read.txt","r") as file:
   # TODO
   for i in file.read():
      if i!=" " and i!="\n":
         temp_string+=i
      elif i=="\n":
         data.append(temp_string)
         temp_string=""
         data.append(i)
      else:
         data.append(temp_string)
         temp_string=""
   data.append(temp_string)
with open("read.txt","r") as file:
   for i in file.readlines():
      print(i,end="\n")
for i in range(1,len(data)+1,4):
   S_h+=eval(data[i])
A_h=S_h/(data.count("\n")+1)
for i in range(2,len(data)+1,4):
   S_w+=eval(data[i])
A_w=S_w/(data.count("\n")+1)
for i in range(1,len(data)+1,4):
   Height.append(data[i])
for i in range(2,len(data)+1,4):
   Weight.append(data[i])
print(f"Average height: {A_h:.2f}")
print(f"Average weight: {A_w:.2f}")
for i in range(len(data)):
   if data[i]==max(Height):
      print(f"The tallest is {(data[i-1])} with {float(data[i]):.2f}cm")
   if data[i]==max(Weight):
      print(f"The heaviest is {data[i-2]} with {float(data[i]):.2f}kg")