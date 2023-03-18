# TODO
times=eval(input())
for i in range(times):
    temp=input().lower()
    temp_set={i for i in temp}
    temp_set=sorted(temp_set)
    temp_set.remove(" ")
    if len(temp_set)==26:
        print("True")
    else:
        print("False")