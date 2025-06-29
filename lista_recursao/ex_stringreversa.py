# print(''.join(list(reversed('python'))))

i=0
def reversa(palavra):
    if len(palavra)<=1:
        return palavra
    return palavra[-1] + reversa(palavra[:-1])  
        
    
print(reversa('python'))

