"""
PROVA

1 2 4 5 5.1 5.2 5.3 6.1 9 11 11.4 11.8 

calendario

fatoracao só com o for
"""

for i in range(1,12):
    if i==1 and i<6:
        print(i, end=" ")
    if i==5:
        for b in range(1,4):
            print(f"{i}.{b}", end=" ")
    if i==6:
        print(f"{i}.{1}")
    if i==7 or i==8 or i==10:
        pass
    if i==9:
        print(i, end=" ")
    if i==11:
        print(i, end=" ")
        for l in range(1,3):
            print(f"{i}.{4*i}", end=" ")
            

