notas = []

contador = 1

while contador<5:
    notas.append(float(input(f"Digite a {contador} nota: ")))
    contador +=1

maior_nota = max(notas)
menor_nota =min(notas)

media=sum(notas)/len(notas)

print(f"A media final é {media:.2f} a maior nota foi {maior_nota:.2f} e a menor nota {menor_nota:.2f}")


