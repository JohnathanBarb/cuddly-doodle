# cuddly-doodle
Teste técnico para entrevista Python + testes

## Descrição do teste

Essa é uma aplicação responsável pelo processamento de pagamentos. E hoje ela tem a capacidade de processar dois tipos de pagamentos, pagamentos utilizando cartão de crédito e pagamentos utilizando cartão de débito.

Nossa empresa entrou tarde na adoção do PIX e precisamos implementar esse novo gateway na aplicação.


### Instalação do projeto

O projeto foi pensado para ser executado utilizando `python3.12` e o `poetry` como gerenciador de pacotes e gerenciador da aplicação.

Idealmente deveriamos utilizar o `poetry` instalado via `pipx` para manter o poetry separado dos arquivos do projeto. E utilizamos `make/Makefile` para encurtar alguns comandos que vão ser bem utilizados.

## Requisição à aplicação

```sh
curl -X POST localhost:8000/api/payment/process \
    -H 'Content-Type: application/json' \
    -d '{
        "store_document": "111",
        "purchaser_document": "222",
        "purchase_value": "10.01",
        "payment_method": "credit_card"}
    '
```
