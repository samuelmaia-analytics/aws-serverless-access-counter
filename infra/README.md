# Infraestrutura

Este diretório foi reservado para a implementação futura da infraestrutura como código do projeto **Contador de Acessos Serverless na AWS**.

A arquitetura pode ser provisionada com uma das seguintes abordagens:

- **AWS CDK**: definição da infraestrutura usando uma linguagem de programação.
- **AWS CloudFormation**: criação dos recursos por meio de templates declarativos.
- **Terraform**: provisionamento multiambiente com arquivos declarativos.

Recursos previstos para implementação:

- Bucket Amazon S3 para hospedagem do frontend estático.
- Amazon API Gateway para expor o endpoint HTTP.
- Função AWS Lambda para executar a lógica do contador.
- Tabela Amazon DynamoDB para armazenar o total de acessos.
- Permissões AWS IAM seguindo o princípio do menor privilégio.
- Logs e métricas no Amazon CloudWatch.

Nenhuma credencial AWS deve ser adicionada neste repositório. Configurações sensíveis devem ser mantidas em variáveis de ambiente, perfis locais da AWS CLI ou ferramentas seguras de gerenciamento de segredos.
