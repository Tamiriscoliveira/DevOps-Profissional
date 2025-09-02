
dig = input('Digite o número 0, você tem 3 tentativas:')
tent = 3 #número de tentativas permitidas
while (dig != '0') and (tent >= 1): #monitora o que foi digitado e também número de tentativas para decidir se encerra o laço
    print('Você não obedeceu! Que coisa!')
    tent = tent - 1
    dig = input('Digite o número 0, você tem '+str(tent)+' tentativas:')
if tent >= 1: #Significa que o laço encerrou antes de esgotar as tentativas
    print('Muito bem!')
else:
    print('Tentativas esgotadas...')