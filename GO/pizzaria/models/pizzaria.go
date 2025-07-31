package models

// quando os atributos esta em letra minuscula no go ele fica no modo privado.

type Pizza struct {
	ID    int     `json:"id"` //referencia em json para conseguir disponibilizar na api
	Nome  string  `json:"nome"`
	Preco float64 `json:"preco"`
}
