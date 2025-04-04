

x = 9
raiz = x ** 2

lado1 = int(input("Digite um lado do triângulo: "))
lado2 = int(input("Digite o outro lado do triângulo: "))

h = ((lado1**2)+(lado2**2))
hipotenusa = h**0.5

print(f"A hipotenusa é: {hipotenusa}")

a = int(input("Digite a: "))
b = int(input("Digite b: "))
y = int(input("Digite y: "))

raiz_y = y**0.5
raiz_b = ((b/2*a)**0.5)
x = ((raiz_y + a/3)/raiz_b)
resultado = x**1/3
print(resultado)
