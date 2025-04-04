
a = float(input("Digite o a da equação: "))
b = float(input("Digite o b da equação: "))
c = float(input("Digite o c da equação: "))

delta = (((b*b)-4*a*c)**0.5)

if delta>0:
    x1 = (-b + delta)/(2*a)
    x2 = (-b - delta)/(2*a)
    print("A raiz 1 é: ", x1)
    print("A raiz 2 é: ", x2)
else:
    print("Delta negativo")




