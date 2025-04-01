z = int(input("Digite o valor de z: "))
w = int(input("Digite o valor de w: "))

if w>0 or z<7:
    x = (5*w+1)/3
    t = 5*z+2
else: 
    x = 5*z+2
    t = (5*w+1)/3

y = (7*x*2-3*x-8*t)/(5*(x+1))
print(y)