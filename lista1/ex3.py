numero = int(input("digite um número: "))

if 20>=numero>=0 and 0<=numero<=15:
    print("O número está no intervalo de 0 a 20 e de -100 a 15")
elif -5<numero<-1 and -100<=numero<=-1:
    print("está no intervalo de -5 a -1 e de -100 a 15")
elif 21<numero<=60:
    print("está no intervalo de 21 a 60")
elif -100<numero<15:
    print("está no intervalo de -100 a 15") 
elif 20>numero>0: 
    print("está no intervalo de 0 a 20")
else: 
    print("o número não está no intervalo")
