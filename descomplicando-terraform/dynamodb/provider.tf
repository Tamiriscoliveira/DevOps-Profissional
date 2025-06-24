terraform {

  backend "s3" {
    bucket = "aula-terraform-tamiris"
    key    = "aula-dynamodb"
    region = "us-east-1"

  }

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 5.100.0" //alterado devido a erro na configuração de duas regiões.
      // version = "~> 5.0"
    }
  }
}

# Configure the AWS Provider
provider "aws" { //provider default
  region = "us-east-1"
}


