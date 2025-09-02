//providers
provider "aws" {
  region = "us-east-1"
}



//backend
terraform {
  backend "s3" {
    bucket  = "aula-terraform-tamiris"
    key     = "test"
    region  = "us-east-1"
    encrypt = true

  }

}



//comando que altera o backend 
//terraform init -migrate-state
//terraform init -reconfigure
//terraform state pull >> aula-backend.tfstate 

//dynamodb_table = "state-lock_dynamodb_terraform" //para arquivo de lock state
