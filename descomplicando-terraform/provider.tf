terraform {

  backend "s3" {
    bucket         = "aula-terraform-tamiris"
    key            = "aula-backend"
    region         = "us-east-1"
    dynamodb_table = "aula_dynamodb_terraform"
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

provider "aws" { // usando alias para utilizar multiplas regiões.
  alias  = "west"
  region = "us-west-2"
}

# Create a VPC
resource "aws_vpc" "example" {
  cidr_block = var.cidr_block
}
