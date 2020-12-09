import random
import os 

name = str(input("digite o seu nome: "))
erros = 0
sorteado=random.randrange(0,50)
jogador=int(input("Digite um número: "))

while(sorteado!=jogador):
    os.system('cls') 
    # comando para limpar a tela no whin
    if(sorteado>jogador):
        print("ERRO, o número é maior")
    elif(sorteado<jogador):
        print("ERRO, o número é menor")
    
    erros+=1 
    # erros = erros+1
    jogador=int(input("Digite um número"))
print("Número digitado: " + str(jogador) + ", parabéns " + str(name) + " você acertou em " + str(erros+1) + " tentativas")

