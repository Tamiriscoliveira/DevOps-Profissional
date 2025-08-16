//providers
provider "aws" {
  region = "us-east-1"
}



//backend
terraform {
  backend "s3" {
    bucket = "aula-terraform-tamiris"
    //dynamodb_table = "state-lock_dynamodb_terraform"
    key    = "test"
    region = "us-east-1"
  }
}





//comando que altera o backend 
//terraform init -migrate-state
//terraform init -reconfigure
//terraform state pull >> aula-backend.tfstate 
