while True: #loop infinito
 
 entrada = input('digite 1 e pressione enter: ')

 if  entrada == '1': #se foi digitado o número pedido
    break #encerra o laço while 
 print('obrigada')


#A instrução ou bloco de instruções associado à cláusula "else" é executada no momento 
#em que o teste da condição ao lado da palavra while resultar em False. 
#Portanto, neste exemplo, a mensagem "Repetição encerrada" aparece quando o usuário 
#digitar qualquer coisa diferente da letra "s".

denovo = True
while denovo:
    op = input('Digite s para repetir:')
    if op != 's':
      denovo = False
else:
    print('Repetição encerrada')