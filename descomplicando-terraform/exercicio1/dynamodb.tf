//configuração para subir um dynamodb para configurar um state lock

resource "aws_dynamodb_table" "state-lock_dynamodb_terraform" {
  name           = "state-lock_dynamodb_terraform"
  hash_key       = "LockID"
  read_capacity  = 20
  write_capacity = 20


  attribute {
    name = "LockID"
    type = "S"
  }

  tags = {
    Name = "DynamoDB Terrafomr State Lock Table"
  }

}
