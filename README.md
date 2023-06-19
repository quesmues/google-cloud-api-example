# Google Cloud API Example

O projeto é sobre a utilização de uma API que retorna dados da Fipe, onde utilizamos o Google Cloud Run, Cloud Build, Cloud Tasks, Firestore e o Terraform para provisionar a infraestrutura, foi utilizado FastAPI para criar as API's.

## Começando

Essas instruções permitirão que você obtenha uma cópia do projeto em operação na sua máquina local para fins de desenvolvimento e teste.

Consulte **Implantação** para saber como implantar o projeto.

### Pré-requisitos

Instale o Python 3.10, Terraform 1.4.6 e o Google Cli (lembre-se de configurar suas credenciais).

Consulte **Terraform** para realizar a implementação dos pré requisitos de ambiente.

Consulte **Variáveis de ambiente (Desenvolvimento)** para configurar as váriaveis de ambiente de desenvolvimento.

### Instalação

Para rodar o projeto em seu computador, primeiro instale os depências com:

```
pip install -r app/requirements-dev.txt
```

Iniciar o FastAPI em modo de desenvolvimento:

```
uvicorn app.main:app --reload
```

Para verificar se o projeto está rodando abra no seu navegador e insira o endereço abaixo.

```
http://127.0.0.1:8000/docs
```

Caso retorne o swagger com a documentação do projeto, o projeto está funcionado!

## Terraform

Iniciar um projeto no Google Cloud e informar em variables.tf

Instalar o Google Cloud Build no GitHub.

Ativar Cloud Run, Gerenciador de Secrets e Contas de Serviço na Conta de Serviço do Cloud Build

Criar um diretório contendo os seguintos arquivos de credenciais:

```
infrastructure/credentials/PROJECT_ID.json // Arquivo de credencial do Google Cloud
infrastructure/credentials/github-token-credentials.txt // Token de Acesso Pessoal do GitHub
infrastructure/credentials/secret-key.txt // Chave secreta
```

Configurar as váriaveis e credenciais utilizadas no arquivo variables.tf.

Para implementar o ambiente utilizando o terraform.
Ir para o diretório do infrastructure/ e executar os seguintes comandos:

Obs: Descomentar o arquivo firestore.tf a primeira vez, para iniciar a Firestore

```
terraform init
terraform plan --out "main.tfplan"
terraform apply "main.tfplan"
```

## Variáveis de Ambiente (Desenvolvimento)

Antes de rodar ou implementar o ambiente, copiar o arquivo "app/.env.dsv.example" para "app/.env".

E realizar a configuração conforme abaixo.

```
SECRET_KEY //Chave Secreta
DEBUG //Modo debug do FastAPI

GCP_CERTIFICATE_PATH // Caminho para o certificado, para desenvolvimento local
GCP_PROJECT_ID // ID do projeto criado no Google Cloud
GCP_REGION // Região que será executado a infraestrutura do Google Cloud ex: southamerica-east1
GCP_RUN_SERVICE_NAME // Nome do serviço definido do Cloud Run definido no cloudbuild.yaml
GCP_AUTH_SCOPE // "https://www.googleapis.com/auth/cloud-platform"

FIPE_BASE_API // URL Base da API da FIPE ex: https://parallelum.com.br/fipe/api/v1
```

## Implantação

Consulte **Terraform** para realizar a implementação dos pré requisitos de ambiente.

Configurar as váriaveis de ambiente no cloudbuild.yaml.

Subir uma tag para o repositório configurado em variables.tf, pois foi configurada uma trigger de repositório no GitHub.

## Tests

Os tests foram feitos utilizando o pytest, para executar apenas rodar o comando abaixo.

```
pytest
```

## Construído com

FastAPI, Aiohttp, Terraform e Google Cloud Python API.

## Autor

* **Eduardo Czamanski Rota** - *Trabalho Inicial* - [Eduardo C. Rota](https://github.com/quesmues)
