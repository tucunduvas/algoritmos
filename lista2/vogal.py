frase = input("Digite uma frase: ").lower()
vogal = " "
vogais = 0
for i in frase:
    vogal=i
    if vogal=="i":
        vogais+=1
    if vogal=="a":
        vogais+=1
    if vogal=="e":
        vogais+=1
    if vogal=="o":
        vogais+=1
    if vogal=="u":
        vogais+=1
        
print(f"A frase {frase} têm {vogais} vogais")