

x = "*"
for i in range(3, 0, -1): 
    for j in range(0,i):
        print(x, end= " ")
    for l in range(3):
        for a in range(0,l):
            print(x, end=" ")
    print(" ")
    
    
print(" ii ")
x = "*"
for i in range(3, 0, -1): 
    for l in range(3):
        for a in range(0,l):
            print(x, end=" ")
    print(" ")
    
"""
1 1 1 1 1 
2 2 2 2
3 3 3
4 4
5
1
1 2
1 2 3
1 2 3 4 
1 2 3 4 5


"""
