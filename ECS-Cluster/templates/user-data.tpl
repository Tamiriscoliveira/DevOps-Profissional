#!/bin/bash
#user-data script de inicialização dos nodes.


#escreve o nome do cluster no arquivo de configuração do ecs
echo ECS_CLUSTER=${CLUSTER_NAME} >> /etc/ecs/ecs.config