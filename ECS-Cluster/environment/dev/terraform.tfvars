project_name = "linuxtips-ecs-cluster"

region = "us-east-1"


#### SSM VPC Paramenters #####

ssm_vpc_id = "/Aula-linuxtips-VPC/vpc/vpc_id"

ssm_public_subnet_1 = "/Aula-linuxtips-VPC/vpc/subnet_public_1a"

ssm_public_subnet_2 = "/Aula-linuxtips-VPC/vpc/subnet_public_1b"

ssm_public_subnet_3 = "/Aula-linuxtips-VPC/vpc/subnet_public_1c"

ssm_private_subnet_1 = "/Aula-linuxtips-VPC/vpc/subnet_private_1a"

ssm_private_subnet_2 = "/Aula-linuxtips-VPC/vpc/subnet_private_1b"

ssm_private_subnet_3 = "/Aula-linuxtips-VPC/vpc/subnet_private_1c"


### BALANCER ###

load_balancer_internal = false

load_balancer_type = "application"

### ECS General ###

nodes_ami = "ami-064d66b3fbe47495e"

node_instance_type = "t3a.large"

node_volume_size = "50"

node_volume_type = "gp3"
