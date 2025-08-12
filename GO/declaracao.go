//DECLARAÇÃO DE VARIAVEIS EM GO

package main

import (
	"fmt"
)

// var idade int = 15 //declaração da variavel a nivel do pacote

func main() {
	// var idade = 15 // podemos omitir o tipo de variavel
	// var idade, dia int = 37, 22 //criar mais de uma variável ao mesmo tempo
	//fmt.Println(idade, dia)

	/*	var (
			idade  int
			altura float32
			nome   string
		) //declarar variável mais de uma variavel com tipos diferentes
		idade = 37
		altura = 1.70
		nome = "Tamiris"
		fmt.Println(nome, idade, altura)
	*/

	/*
		//deixando o go inferir os dados
		var (
			idade  = 15
			altura = 1.70
			nome   = "tamiris"
		)
		fmt.Println(nome, idade, altura)
	*/

	// Short variable declarations, ou seja, declarações curtas de variáveis utilizando o sinal : seguido do =.
	//usatemos  quando for atribuir um valor dentro do escopo de uma função
	idade := 15
	altura := 1.78
	nome := "Guilherme"
	fmt.Println(nome, idade, altura)
}
