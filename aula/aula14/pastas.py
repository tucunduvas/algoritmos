import os

def escanear_pastas(pasta_inicial, pasta = ''):
    caminho = os.path.join(pasta_inicial, pasta)
    if not os.path.dir(caminho):
        return 
    arquivos = os.listdir( os.path.join(pasta_inicial, pasta))
    
    for arquivo in arquivos:
        print(arquivo)
        escanear_pastas(pasta_inicial, arquivo)
        
caminho = ''

escanear_pastas(caminho)