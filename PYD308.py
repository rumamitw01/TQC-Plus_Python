# TODO
count=eval(input())
for i in range(count):
    temp_string=input()
    temp=0
    for j in range(len(temp_string)):
        temp+=int(temp_string[j])
    print(f"Sum of all digits of {temp_string} is {temp}")