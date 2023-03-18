# TODO
height=0
weight=0
while height!=-9999 and weight!=-9999:
    height=eval(input())
    weight=eval(input())
    BMI=weight/((height/100)**2)
    if height==-9999 or weight==-9999:
        break
    else:
        print(f"BMI: {BMI:.2f}")
        if BMI<18.5:
            print("State: under weight")
        elif BMI<25 and BMI>=18.5:
            print("State: normal")
        elif BMI<30 and BMI>=25:
            print("State: over weight")
        elif BMI>=30:
            print("State: fat")