# Mini-Projeto - Extração de dados de valores de câmbio da API do BCB

## Descrição

O objetivo do projeto é realizar a extração dos dados de câmbio do dólar (comercial e venda) de acordo com período definido pelo usuário e reforçar os conceitos de manipulação de APIs com a biblioteca **Requests** e de manipulação de dados com **Pandas**. 

Os dados são coletados, tratados e inseridos em um arquivo de formato .CSV. A cada execução realizada pelo usuário, o arquivo é sobrescrito com os dados referentes ao período solicitado.

A API do BCB disponibiliza os dados de segunda-feira à sexta-feira, portanto, as informações obtidas são referentes aos dias úteis.

## Tecnologias utilizadas

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)

## Execução do script

### Instalação do ambiente virtual (venv)

No terminal (Linux/Mac OS), execute os comandos a seguir. Defina o nome do ambiente de acordo com a sua preferência.
``` 
python -m venv nome_do_ambiente
source nome_do_ambiente/bin/activate
```

Caso utilize Windows, substitua o segundo comando por:

``` 
.\nome_do_ambiente\Scripts\activate
``` 

### Instalação das bibliotecas utilizadas

Após a ativação do ambiente virtual, no diretório do projeto, execute o comando a seguir para instalar todas as bibliotecas necessárias para o projeto.

```
pip install -r /path/to/requirements.txt
``` 

### Execução do script

Depois de realizar a instalação das bibliotecas, execute o script **main.py** dentro do diretório de ***scripts***.
``` 
cd scripts
python main.py
``` 

O script solicitará ao usuário a data de início e de término do período para a coleta de dados. Informe a data no formato **MM-DD-YYYY**.

O resultado deve ser:
``` 
Armazenado com sucesso!
``` 

Por fim, verifique os dados armazenados no arquivo **cotacoes_dolar.csv** na pasta ***data***.
