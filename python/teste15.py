#primeira função
def Hello():
    print("Hello World !")


Hello()



#função com argumento
def Hello2(argumento):
    print(argumento)


Hello2("olá mundo")
Hello2("teste---argumento")
Hello2(5+5)



#função com argumentos usando palavra chave
def AddIt(Valor1, Valor2):
    print(Valor1, " + ", Valor2, " = ", (Valor1 + Valor2))


AddIt(2,3)
AddIt(Valor2=3, Valor1=2)


#função com argumentos padrões

def Hello3(saudacao = "olá mundo"):
    print(saudacao)

Hello3("Hello World")
Hello3()


#argumentos variaveis
def Hello4(argumentos, *VarArgs):
    print("5km", "10km", "21km","42km")
    for arg in VarArgs:
        print(arg)


Hello4(1, "test")
Hello4(3, "1", "2", "3")


#retornando informações 
def soma(value1, value2):
    return(value1 + value2)


print("a soma dos valores informado: ",  soma(2,6))
print("2 + 6 e igual a 4 + 4", (soma(2,6)== soma(4,4))) #comparando funções


#função para receber dados
def recebendoDados():
    Nome = input("Digite o seu nome: ")
    print("Seja Bem Vindo(a)", Nome)

recebendoDados()


def salario():
    numero = float(input("Digite o salario: "))
    print("o salário e: ", numero)

salario()