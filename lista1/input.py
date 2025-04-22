nome = input("Insira seu nome: ")
idade = input("insira sua idade: ")

print("Oi, " + nome + "!")
print("Você tem: " + idade + " anos!")

conta_bancaria = int(input("Insira quanto você tem: "))

if conta_bancaria<5:
    print("Pobreta")
else:
    print("Rica")

print(f"Olá , meu nome é {nome} e eu tenho {idade} anos")
print("Oi, " + nome + " você tem " + idade + " anos!")

#leitura e exrita em arquivos

# r leitura
# a anexar 
# w escrever

# para ler um arquivo primeiro precisa abrir com a função open com o modo r 
# depois é possivel ler com os métodos read() ou readlines()

arquivo = open("dados.txt", "r")
conteudo = arquivo.read()
print(conteudo)
arquivo.close()

# para escrever

arquivo = open("dados.txt", "w")
arquivo.write("Tudo bem")
arquivo.close

#no modo de escrever, se o arquivo não existir ele será criado automaticamente, se existir o conteudo sera sobrescrito
#sempre deve fechar

with open("dados.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

"""
    A entrada e saída de dados em Python nos oferece uma grande flexibilidade para interagir com o usuário e 
    manipular arquivos externos. Podemos solicitar informações ao usuário, mostrar resultados na tela e ler 
    ou escrever dados em arquivos de texto. Lembre-se sempre de manejar adequadamente a abertura e fechamento
    de arquivos, e considerar as possíveis exceções que podem ocorrer durante as operações de entrada/saída.
"""


