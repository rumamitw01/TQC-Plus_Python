# TODO
string1=input()
if len(string1)==11:
    for i in range(len(string1)):
        if i==3 or i==6:
            if string1[i]=="-":
                pass
            else:
                print("Invalid SSN")
                break
        else:
            if ord(string1[i])>=48 and ord(string1[i])<=57:
                pass
            else:
                print("Invalid SSN")
                break
    if i==len(string1)-1:
        print("Valid SSN")
else:
    print("Invalid SSN")