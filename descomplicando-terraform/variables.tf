variable "image_id" { //declarar a variavel
  type = string       // forma de garantir qual o tipo de valor que será passado.
  //default = "ami-123456" // se o usuário preciar especificar o ideal e não ter default.
  description = "O ID da AMI usada" // uma documentação sobre a variavel
  validation {                      //condição para fazer validação
    condition     = length(var.image_id) > 4 && substr(var.image_id, 0, 4) == "ami-"
    error_message = "(o valor passado precisa iniciar com ami-)The image_id value must be a valid AMI id, starting with \"ami-\"." //
  }

  sensitive = false // para valores sensiveis

}



// terraform plan -out plano -var="image_id=ami-abc123" para passar via linha de comando o valor da variável
// terraform plan -out plano -var-file="testing.tfvars" para utiizar usando um arquivo
