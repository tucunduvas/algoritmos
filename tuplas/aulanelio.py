# n = int(input("Quantos numeros voce vai digitar? "))
# lista = [0 for x in range(n)]

# for i in range(0,n):
#     lista[i]= int(input("digte um numero: "))
    
# for i in lista:
#     print(i)
    
tupla = 1,2,3,4,5

print(tupla[0:2])
print(tupla[3])

print(tupla[1:]) 
print(tupla[-1])

for n in tupla: 
    print(n)
    
lanche = ('suco', 'hamburgue','pizza', 'refri')
print(lanche[:3])

for cont in range(0,len(lanche)):
    print(lanche[cont])
    
for posicao, comida in enumerate(lanche):
    print(f"eu vou comer {comida} na posicao {posicao}")

print(sorted(lanche)) 

a = 2,5,4
b = 5,8,1,2
c = a+b #juntando tuplas 

print(c.count(2)) #conta quantas vezes o 2 aparaceu
print(c.index(8))# fala em qual posicao esta
print(c.index(5,1))

del(lanche)
#so é possivel apagar a tupla inteira

zero_a_vinte= ('zero','um', 'dois', 'tres', 'quatro', 'cinco','seis','sete','oito','nove','dez','onze','doze', 'treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')


