"""_summary_
    4. (5 Pontos) O Labirinto Temporal Evoluído
Você foi capturado em um labirinto temporal digital, onde só poderá escapar resol-
vendo um enigma numérico complexo. O labirinto possui 12 portais numerados de 1
a 12. Para cada portal, o sistema pedirá que o usuário informe um número inteiro.
A cada entrada, o sistema executará uma análise com as seguintes regras:
· Se o número informado for múltiplo de 4 ou de 6, ele é considerado um impulso
de avanço temporal.
· Se o número for primo e ímpar, ele é considerado uma anomalia de instabili-
dade.
· Se o número for negativo, ele aciona um pulso reverso e deve ser ignorado em
todas as contagens.
Além disso, o sistema monitora eventos críticos:
· Se 3 anomalias consecutivas forem detectadas, o sistema exibe "Colapso
temporal! Experimento falhou." e encerra imediatamente.
· Se o total de impulsos de avanço temporal for menor que 5 ao final dos 12
portais, o sistema exibirá "Estabilidade insuficiente. Viagem temporal
negada. ".
Se o usuário concluir os 12 portais sem nenhum colapso e com impulsos suficientes, o
sistema deve exibir:
Impulsos de avanço: X
Anomalias de instabilidade: Y
Sistema estabilizado. Liberação autorizada.
Restrições: Não é permitido o uso de listas. Todos os controles devem ser feitos
com variáveis acumuladoras e estruturas de repetição (for e/ou while). A verifi-
cação de número primo deve ser feita manualmente. Números negativos devem ser
desconsiderados nas regras principais.
    """
impulso = 0
anomalia = 0
    

        
i=1  
while i<13:
    num = int(input("digite um número inteiro: "))
    if num%4==0 and num%6==0:
        impulso +=1
    if num%2!=0 or num==2:
        anomalia += 1
        if anomalia == 3:
            print("Colapso temporal! Experimento falhou.")
            break
    i+=1
if impulso<5:   
    print("Estabilidade insuficiente. Viagem temporal negada.")  
    
if impulso==0 and anomalia==0:
    print(f"impulsos: {impulso}")
    print(f"Anomalias: {anomalia}")
    """_summary_
    · Se o total de impulsos de avanço temporal for menor que 5 ao final dos 12
portais, o sistema exibirá "Estabilidade insuficiente. Viagem temporal
negada. ".
    """