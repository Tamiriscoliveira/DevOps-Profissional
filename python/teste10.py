contador = 1 #cria variável contador com valor 1

while contador <= 5: #enquanto contador for menor que 5, repete bloco
    print(contador)
    contador = contador + 1
print('fim do programa')


cont = 10 #cria variável de controle, iniciando com valor 10
min = 1 #cria variável que representa limite inferior, com valor 1
while cont >= min: #repete enquanto uma variável for maior ou igual à outra
    print(cont, end="... ") #exibe variável de controle
    cont = cont - 1 #reduz seu valor em um
print('Foguete lançado!') #mensagem final

tarefas = ['Organizar', 'Investir', 'Ler']
while len(tarefas) > 0: #Enquanto comprimento da lista é maior que zero, ou seja, enquanto a lista ainda tem elementos
    print(tarefas[0]) #Exibe o primeiro elemento, do índice 0
    tarefas.pop(0) #Remove o primeiro elemento


    digitado = input('Digite o número 0 e pressione Enter para encerrar o programa:')
while digitado!='0':
    print('Você não quis encerrar o programa! Que rebeldia... gostei!')
    digitado = input('Digite o número 0 e pressione Enter para encerrar o programa:')
print('Programa encerrado')

