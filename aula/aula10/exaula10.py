import random
from random import randint

#gere 100 numeros randomicos, de 20 a 100, filtre os maiores que 60
##gere 100 numeros randomicos, de 20 a 100, filtre os maiores que a media desses numeros
#gere 100 numeros randomicos, de 20 a 100, filtre os menores que 25

numeros = [ randint(20,100) for x in range(100)] 

maiores_60 = list(filter(lambda x: x>60, numeros))

print("Ex 1 - números maiores que 60: ", maiores_60)

maiores_media = list(filter(lambda x: x>(sum(numeros)/len(numeros)), numeros))

print(f"Ex 2 - números maiores que a média {sum(numeros)/len(numeros)}: ", maiores_media)

menores_25 = list(filter(lambda x: x<25, numeros))

print(f"Ex 2 - números menores que 25: ", menores_25)


