# State no Terraform

O state é a forma de armazenar informações que são manipuladas.

O Terraform não funciona sem o state.

Serve para mapear o "mundo real", ou seja, o que está na cloud.

O metadata faz o mapeamento das dependências.

# Comandos relacionados ao state

terraform state list → lista os recursos existentes no state.

terraform refresh → sincroniza o state caso tenha algum recurso criado manualmente.

terraform state pull → baixa todo o state remoto.

terraform import → importa recursos já existentes na cloud para o state.
⚠️ Apenas importa para o state, não gera código automaticamente.

# Workspaces

O workspace é uma forma de manipulação do state.

Permite apontar para o mesmo backend utilizando múltiplas instâncias.

terraform workspace → cria vários ambientes, cada um com um state diferente.
👉 Ou seja, trabalha apenas a nível de state, não do código.

# Questões

Qual nome do módulo padrão que é criado quando não se especifica explicitamente?
R: Root module

Para fins de segurança, qual o melhor lugar para manter um state file?
R: Remoto

Qual comando é utilizado para atualizar o state file com base no "mundo real" do provider?
R: terraform refresh

Qual comando é utilizado para importar informações de recursos já existentes na cloud e colocar no state file?
R: terraform import

Os recursos criados em workspaces diferentes estão separados automaticamente no provider?
R: Não

# Dependência entre recursos

A ideia é que um recurso saiba o momento exato em que deve ser criado ou atualizado, respeitando a ordem correta.

Dependências Implícitas → determinadas automaticamente pelo Terraform, a partir de referências diretas entre recursos.

Dependências Explícitas → declaradas manualmente pelo utilizador com depends_on.


# manipular o modo verbose do comando

passa a variavel de ambiente: TF_LOG

níveis de logs: TRACE, DEBUG, INFO, WARN ou ERROR

 TF_LOG=DEBUG terraform plan


 comando taint serve para marcar que um recurso precisa ser destruindo e recriado, ele faz uma marcação  para que 
 após plan e o apply.



   sudo apt install graphviz
  terraform graph | dot -Tsvg > graph.svg


  terraform -chdir=/home/tamiris/DevOps-Profissional/descomplicando-terraform plan

  com a opção -chdir é possivel executar arquivos .tf mesmo estão em outro diretorio. Por exemplo: meu diretorio atual esta em /home/tamiris posso executar arquivos que estão no diretorio /var/teste/


  Um diretório de trabalho deve ser inicializado antes que o Terraform possa executar qualquer operação nele (como provisionar infraestrutura ou modificar estado).