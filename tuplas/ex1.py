while True:
    num = int(input("qual numero entre 0 e 20 vc deseja ver: "))
    if num<0 or num>20:
        num = int(input("numero inválido, tente novamente: "))
    if 20>=num>=0:
        print(f"Você digitou o número {zero_a_vinte[num]}")
        break