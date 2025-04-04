saldo_medio = float(input("Informe o saldo médio: "))

if 200>=saldo_medio>=0: 
    print("Saldo médio: ",saldo_medio ,"Nenhum crédito disponível.")
elif 400>=saldo_medio>=201:
    credito = saldo_medio*0.2
    print("Saldo médio: ", saldo_medio ,"Crédito disponível: ", credito)
elif 401<=saldo_medio<=600:
    credito = saldo_medio*0.3
    print("Saldo médio: ", saldo_medio ,"Crédito disponível: ", credito)
else: 
    credito = saldo_medio*0.4
    print("Saldo médio: ", saldo_medio ,"Crédito disponível: ", credito)