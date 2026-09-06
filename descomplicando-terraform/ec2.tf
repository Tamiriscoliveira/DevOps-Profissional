
data "aws_ami" "ubuntu" {
  most_recent = true

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-*"]
  }

  owners = ["099720109477"] # Ubuntu
}




resource "aws_instance" "web" {
  // ami = "ami-0885b1f6bd170450c" // imagem utilizada para criar a instance
  // ami  = data.aws_ami.ubuntu pea todos val
  // ami           = data.aws_ami.id
  ami = var.image_id
  instance_type = "t2.micro"

  tags = {
    Name       = "Hello-World"
    enviroment = "Dev"

  }

}


resource "aws_instance" "webohio" {
  ami = "ami-0885b1f6bd170450c" // imagem utilizada para criar a instance
  // ami  = data.aws_ami.ubuntu pea todos valores
  // ami           = data.aws_ami.id
  instance_type = "t2.micro"
  provider = aws.ohio

  tags = {
    Name       = "Hello-World"
    enviroment = "Dev"
    worksapce = terraform.workspace

  }

}
