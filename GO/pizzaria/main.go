package main

import (
	"encoding/json"
	"fmt"
	"os"
	"pizzaria/models"
	"strconv"

	"github.com/gin-gonic/gin"
)

var pizzas []models.Pizza

//{
//{ID: 1, Nome: "Toscana", Preco: 49.5},
//{ID: 2, Nome: "Marguerita", Preco: 79.5},
//{ID: 3, Nome: "Atum com queijo", Preco: 69.5},
//}

// criando endpoints
func main() {
	loadPizzas()
	router := gin.Default()
	router.GET("/pizzas", getPizzas)
	router.POST("/pizzas", postPizzas)
	router.GET("/pizzas/:id", getPizzasByID)
	router.Run()
}

// primeira função fora da principal(main)
func getPizzas(c *gin.Context) {

	c.JSON(200, gin.H{
		"pizzas": pizzas,
	})
}

// criando funcao para inserir dados
func postPizzas(c *gin.Context) {
	var newPizza models.Pizza
	if err := c.ShouldBindJSON(&newPizza); err != nil {
		c.JSON(400, gin.H{
			"erro": err.Error()})
		return
	}
	newPizza.ID = len(pizzas) + 1
	pizzas = append(pizzas, newPizza)
	savePizza()
	c.JSON(201, newPizza)
}

func getPizzasByID(c *gin.Context) {
	idParam := c.Param("id")
	id, err := strconv.Atoi(idParam)
	if err != nil {
		c.JSON(400, gin.H{
			"erro": err.Error()})
		return
	}
	for _, p := range pizzas {
		if p.ID == id {
			c.JSON(200, p)
			return
		}
	}
	c.JSON(404, gin.H{"message": "Pizza not found"})
}

func loadPizzas() {
	file, err := os.Open("dados/pizza.json")
	if err != nil {
		fmt.Println("Error file:", err)
		return
	}
	defer file.Close()

	decoder := json.NewDecoder(file) //funcao capaz de interpretar arquivos json
	if err := decoder.Decode(&pizzas); err != nil {
		fmt.Println("Error decoding JSON:", err)
	}
}

func savePizza() {
	file, err := os.Create("dados/pizza.json")
	if err != nil {
		fmt.Println("Error file:", err)
		return
	}
	defer file.Close()

	encoder := json.NewEncoder(file)
	if err := encoder.Encode(pizzas); err != nil {
		fmt.Println("Error encoding JSON", err)

	}

}

// A função Decode é utilizada para decodificar dados JSON e carregá-los em uma estrutura Go,
//enquanto Encode é usada para codificar uma estrutura Go e salvá-la em formato JSON.
/*
A Linguagem de Programação Go - https://go.dev/tour/welcome/1
Go no Google: Design de Linguagem a Serviço da Engenharia de Software -  https://go.dev/talks/2012/splash.article
Padrões de Concorrência em Go - https://go.dev/blog/waza-talk
Sintaxe de Declaração do Go -  https://go.dev/blog/declaration-syntax
A Evolução do Go - https://go.dev/blog/randv2
O Caminho para o Go 2 - https://go.dev/blog/go2-here-we-come
Erros são Valores -  https://go.dev/blog/errors-are-values
Estruturas de Dados em Go: Interfaces - https://research.swtch.com/interfaces
*/
