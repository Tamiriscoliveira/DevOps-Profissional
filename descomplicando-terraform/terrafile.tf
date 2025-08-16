module "servers" {
  //tudo que não for source, version e providers, são inputs.
  source  = "./servers"
  servers = 1
}


// exportando output do modulo filho
output "ip_address" {
  value = module.servers.ip_address

}
