output "load_balancer_dns" {
  value = aws_lb.main.dns_name

}

output "lc_ssm_arn" {
  value = aws_ssm_parameter.lb_arn.id
}


output "lc_ssm_listener" {
  value = aws_ssm_parameter.lb_listener.id
}
