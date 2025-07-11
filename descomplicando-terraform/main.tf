data "aws_ami" "ubuntu" {
  most_recent = true

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-*"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }

  owners = ["099720109477"] # Canonical
}

resource "aws_instance" "web" {
  // ami           = data.aws_ami.ubuntu.id
  ami           = var.image_id //como usar a variavel
  instance_type = "t3.micro"

  tags = {
    Name       = "HelloWorld"
    Plataforma = data.aws_ami.ubuntu.platform_details
    Env        = "develop"
  }
}


resource "aws_instance" "webest" {
  //ami           = data.aws_ami.ubuntu.id
  ami           = var.image_id
  instance_type = "t3.micro"
  provider      = aws.west
  tags = {
    Name       = "HelloWorld"
    Plataforma = data.aws_ami.ubuntu.platform_details
    Env        = "develop"
  }
}

//terraform state list para verificar os objetos dentro do state
//terraform state show data.aws_ami.ubuntu
//terraform state pull | jq
// terraform state pull | jq .availability_zone
