# uma alternativa mais simples, que apenas resulte em True ou False, basta usar 
#o operador "in". A seguir exemplificamos o uso deste operador, usando-o dentro de 
# uma expressão lógica testada na estrutura "if".
#Lembrando que operadores normalmente podem ser combinados para gerar expressões, outra 
#forma comum de uso do operador "in" é combinando-o com operador "not", gerando então 
#a expressão "not in", que resulta em True justamente se o elemento NÃO estiver presente 
#na lista em questão.

lista = ['teste', 123, 44.44]
elemento = 'teste'
if elemento in lista: #resultará em True
    print('O elemento', elemento, 'EXISTE na lista')
else:
    print('O elemento', elemento, 'NÃO existe na lista')
elemento = 'abc' #segundo teste
if elemento in lista: #resultará em False
    print('O elemento', elemento, 'EXISTE na lista')
else:
    print('O elemento', elemento, 'NÃO existe na lista')


#alguns métodos interessantes:
#.clear() - apaga todos os elementos da lista, deixando-a vazia
#.reverse() - inverte a ordem dos elementos, os últimos elementos se tornam os primeiros e vice-versa
#.sort() - ordena os elementos, do menor para o maior

vogais = ['a', 'e', 'i', 'o', 'u']
vogais.clear() #limpa a lista, remove todos os elementos
print(vogais) #exibe []
nums = [10, 5, 12, 7, 3, 15]
nums.reverse() #inverte a ordem, a posição, dos elementos
print(nums) #exibe [15, 3, 7, 12, 5, 10]
nums.sort() #ordena lista de forma crescente
print(nums) #exibe [3, 5, 7, 10, 12, 15] 



#Outra ferramenta que pode ser bastante útil é o "slicing" das listas, ao qual vou me 
#referir como "fatiamento" de listas. Nesta operação, informamos uma faixa, um intervalo, 
#ao invés de um único valor inteiro como índice, e geramos uma cópia dos elementos 
#posicionados naquele intervalo. A sintaxe deste intervalo índices, desta "fatia" da 
#lista, possui pelo menos um símbolo de : (dois pontos), com um valor de índice inicial 
#antes dele, e um valor limite depois. Vou tentar esclarecer com um exemplo, cujo código 
#podes observar logo abaixo. Neste exemplo, a lista declarada na primeira linha possui 5 
#elementos, porém ao usar lista[1:4] na última linha do código, estamos selecionando para 
#exibição apenas a parte dos elementos que iniciam no índice 1 (incluindo o 1) e vão até 
#o índice 4 (excluindo o 4, ou seja, até 3).
#E mais do que apenas selecionar os elementos na lista já existente, esta operação de 
#slicing (ou fatiamento) faz uma cópia de todos estes elementos, gerando uma nova lista 
#como resultado, o que nos permite realizar atribuições conforme demonstrado o próximo
#exemplo de código-fonte.


lista = [11, 22, 33, 44, 55] #índices 0, 1, 2, 3, 4
print(lista) #exibe [11, 22, 33, 44, 55]
print(lista[1:4]) #exibe elementos do índice 1 (incluso) até índice 4 (excluso), ou seja, [22, 33, 44]


lista_A = [11, 22, 33, 44, 55]
lista_B = lista_A[0:3] #cria lista com cópia dos elementos do índice 0 (incluso) até índice 3 (excluso) da lista_A
print(lista_B) #exibe [11, 22, 33]
lista_A[0] = 88 #altera primeiro elemento da lista_A
lista_B[0] = 99 #altera primeiro elemento da lista_B
print(lista_A) #exibe [88, 22, 33, 44, 55]
print(lista_B) #exibe [99, 22, 33]
