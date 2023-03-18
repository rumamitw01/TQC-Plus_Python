# TODO
def compute(a,b,c):
    delta=b**2-4*a*c
    if delta<0:
        return "Your equation has no root."
    elif delta==0:
        return -(b/(2*a)),-(b/(2*a))
    else:
        return (-b+(b**2-4*a*c)**0.5)/(2*a),(-b-(b**2-4*a*c)**0.5)/(2*a)
a=eval(input())
b=eval(input())
c=eval(input())
if compute(a,b,c)[0]==compute(a,b,c)[1]:
    print(compute(a,b,c)[0])
elif type(compute(a,b,c))==str:
    print(compute(a,b,c))
else:
    print(f"{compute(a,b,c)[0]}, {compute(a,b,c)[1]}")