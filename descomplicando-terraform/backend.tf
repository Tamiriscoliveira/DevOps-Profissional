//bloco do backend
# state.tf
terraform {
  backend "s3" {
    bucket = "aula-terraform-tamiris"
    key    = "aula4-devopsProfissional"
    region = "us-east-1"
  }
}
