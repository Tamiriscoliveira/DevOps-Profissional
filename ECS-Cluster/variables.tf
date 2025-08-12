### General Configs ###

variable "project_name" {}

variable "region" {}

### SSM VPC ###

variable "ssm_vpc_id" {}

variable "ssm_public_subnet_1" {}

variable "ssm_public_subnet_2" {}

variable "ssm_public_subnet_3" {}

variable "ssm_private_subnet_1" {}

variable "ssm_private_subnet_2" {}

variable "ssm_private_subnet_3" {}


### BALANCER ###

variable "load_balancer_internal" {} #Define se o Load Balancer deve ser interno (true) ou externo (false).

variable "load_balancer_type" {} # O tipo de Load Balancer a ser criado (ex: 'application' ou 'network').


