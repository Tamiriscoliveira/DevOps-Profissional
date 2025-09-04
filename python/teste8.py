minha_lista_vazia=[]
print(minha_lista_vazia)

minha_lista_exemplo=[1231, "tamiris", True]
print(minha_lista_exemplo)

# exemplo de lista dentro de lista
lista_de_animais = ['coruja', 'golfinho', ['gato', 'gata'], 'cobra']
print(lista_de_animais)

frutas = ['Banana', 'Laranja', 'Maçã', 'Tomate']
print(frutas[1])
print(frutas[-1])


nomes = ['Paulo', 'Fernanda', 'Danilo']
primeiro_nome = nomes[0] #guarda cópia do primeiro elemento da lista 
print(primeiro_nome) #exibe Paulo
sobrenomes = ['Silva', 'Medeiro', 'Cruz']
#abaixo exemplo de operação que utiliza alguns elementos das listas
primeiro_nome_completo = nomes[0] + ' ' + sobrenomes[0] 
print(primeiro_nome_completo) #exibe Paulo Silva


nomes[2] = 'Laila' #altera terceiro elemento (nesse caso último)
print(nomes) #exibe ['Paulo', 'Fernanda', 'Laila']
nomes[-1] = 'Maitê' #altera último elemento
print(nomes) #exibe ['Paulo', 'Fernanda', Maitê]


nums = [10, 20] #cria lista com dois elementos
nums.append(11) #adiciona o valor 11 ao final da lista numeros
nums.append(7) #adiciona o valor 7 ao final da lista numeros
print(nums)


numeros = [10, 20] #cria lista com dois elementos
numeros.insert(0, 5) #insere valor 5 no índice 0, desloca demais valores para a direita
print(numeros) #exibe [5, 10, 20]

numeros.insert(10, 33) #tenta inserir em índice maior que lista, o que acaba inserindo ao final
print(numeros) #exibe [5, 10, 20, 33]numeros.insert(2, 7) #insere valor 7 no índice 2, desloca demais valores para a direita

numeros.insert(2, 7) #insere valor 7 no índice 2, desloca demais valores para a direita
print(numeros) #exibe [5, 10, 7, 20, 33]


lista = ['eu', 'tu', 'ele', 'nós'] #cria lista com quatro elementos
lista.pop() #remove o último elemento
print(lista) #exibe ['eu', 'tu', 'ele']
lista.pop(1) #remove o segundo elemento, no índice 1
print(lista) #exibe ['eu', 'ele']


lista2 = ['eu', 'tu', 'ele', 'nós'] #cria lista com quatro elementos
ultimo = lista2.pop() #remove e retorna o último elemento da lista, que é armazenado então na variável ultimo
print(ultimo) #exibe 'nós'


lista1 = [] #cria uma lista vazia
print('Tamanho da lista:', len(lista1)) #exibe 'Tamanho da lista: 0
lista1.append('teste') #adiciona um elemento à lista1
print('Tamanho da lista:', len(lista1)) #exibe 'Tamanho da lista: 1
lista2 = ['a', 'b', 'c', 'd', 'e'] #cria uma lista com 5 elementos
tamanho = len(lista2) #armazena tamanho atual da lista2 em uma variável
print('Tamanho da lista:', tamanho) #exibe 'Tamanho da lista: 5


#Os métodos .index() e .count() são úteis quando desejamos procurar por um elemento na 
# lista, e/ou pelo menos verificar se um elemento está presente nela.
# O .index() espera receber o valor de um elemento dentro dos seus parênteses, e então 
# procurará por esse elemento na lista, retornando o índice da primeira ocorrência 
# encontrada, como exemplificado no código abaixo.

impares = [1, 3, 5, 7, 9, 7] #cria uma lista com 6 elementos do tipo inteiro
indice = impares.index(7) #retorna 3, que é o índice do primeiro valor 7 encontrado nesta lista
print(indice) #exibe 3


#Mas atenção! Utilize o .index() apenas quando tiveres certeza de que o elemento está 
#presente na lista, ou ocorrerá um erro de execução! Uma alternativa mais segura 
#neste sentido é o método .count(), que conta a quantidade de vezes que o elemento 
#passado como argumento aparece na lista. Ou seja, caso o elemento não esteja presente, 
#o método apenas resultará no valor 0, sem causar erro. 
#Observe como o código a seguir traz alguns testes demonstrativos deste método.

li = ['a', 'b', 'a', 'abc', 'aeiou', '01010'] #cria uma lista com alguns elementos tipo string
print(li.count('a')) #exibe 2, pois encontrou duas veze este elemento na lista
print(li.count('zz')) #exibe 0, pois não encontrou este elemento na lista