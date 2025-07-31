package main

import (
	"esporte/models"

	"strconv"

	"github.com/gin-gonic/gin"
)

var esporte = []models.Esporte{
	{ID: 1, Nome: "Corrida"},
	{ID: 2, Nome: "Ciclismo"},
	{ID: 3, Nome: "Soccer"},
}

func main() {
	router := gin.Default()
	router.GET("/esporte", getEsportes)
	router.GET("/esporte/:id", getesporteByID)
	router.Run()
}

func getEsportes(c *gin.Context) {

	c.JSON(200, gin.H{
		"esporte": esporte,
	})
}

func getesporteByID(c *gin.Context) {
	idParam := c.Param("id")
	id, err := strconv.Atoi(idParam)
	if err != nil {
		c.JSON(400, gin.H{
			"erro": err.Error()})
		return
	}
	for _, l := range esporte {
		if l.ID == id {
			c.JSON(200, l)
			return
		}
	}
	c.JSON(404, gin.H{"message": "Esporte não encontrado"})
}
