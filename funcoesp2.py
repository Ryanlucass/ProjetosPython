
# argumentos dentros das funções
# a função recebe os argumentos de entrada
# ele vai somar todos so argumentos de entrada que eu colocar, já que o r+=n soma todos os argumentos em cima do outro
def somar(*num):
    r=0
    for n in num:
        r+=n

    print("Soma = " + str(r))
    




# irá imprimir todos os argumentos de uma função
# argumentos arbitrários

def default(*txt):
    for t in txt:
        print(t)


def carros(c="gol"):
    
    print("Modelo: "+c)
    
    

# chama das funções:


carros()
# somar(3,4,5,6,7,8,8,6,4)