//bloco do backend
terraform {
  backend "local" {
    path = "/home/tamiris/DevOps-Profissional/descomplicando-terraform/terraform.tfstate"
  }
}
