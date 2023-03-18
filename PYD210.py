side1 = eval(input())
side2 = eval(input())
side3 = eval(input())
side_sum=side1+side2+side3
side_list=[side1,side2,side3]
side_list=sorted(side_list)
#TODO
if side_sum-side_list[2]>side_list[2]:
    print(side_sum)
else:
    print("Invalid")