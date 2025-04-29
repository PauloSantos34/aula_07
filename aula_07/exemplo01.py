# Funçoes em python inicia com a palavra
# reservada "def".
# Funçôes são rotinas em seu conceito.
# São blocos de códigos que só serão executados, se forem chamados. 

# def saudacao():
# print('Olá mundo!')

#saudacao()
#saudacao()
#saudacao() 
    
# def mostrar_linha():
    # print(30*"=")    

# mostrar_linha()
# print('MÓDULO 01')
# mostrar_linha()
# print('ALGORITIMOS')
# mostrar_linha()
# print('ANÁLISE DE DADOS')
    
# def saudacao(texto):
# print(f'Olá {texto}!')

# nome = input('Informe o nome: ')

# saudacao(nome)


def somar_numeros(x, y):
    s = x + y
    return s


for i in range(3):
    n1 = int(input('Informe o número: '))
    n2 = int(input('Informe o número: '))

    soma = somar_numeros(n1, n2)
    print(soma)




