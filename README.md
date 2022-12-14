# Exemplos de scripts para extração de dados

## Pré-requisitos

- Python 3.9

Clone o projeto e instale as dependências:

```bash
python -m venv venv
python -m pip install -r requirements.txt
```

## Extração de dados SIA/SUS

Para executar a geração dos dados a partir do tabnet, executar o arquivo [main.py](main.py)

```bash
python main.py
```

A extração é feita por mês e município.

O script:

1. Executa um post na página do tabnet em http://tabnet.datasus.gov.br/cgi/tabcgi.exe?sia/cnv/qbam.def

2. Utiliza o BeautifulSoup para extrair a tabela html formatada.

3. Faz a limpeza do campo procedimento, removendo espaços desnecessários e adiciona as colunas de compentencia e municipio.

4. Gera um arquivo csv com esses dados.

## Combinando os arquivos CSV mensais

O arquivo [combine.py](combine.py) combina todos os arquivos da pasta data em um só.

# Redash

Podemos utilizar o [redash](https://github.com/getredash/redash) para visualizar os dados.

## Pré-requisitos

Docker e docker-compose instalados

## Executando localmente

Crie um arquivo chamado `.env` e atualize os valores conforme a necessidade. Utilize o arquivo [.env-example](.env-example) como exemplo.

Em seguida, execute os comandos:

```bash
docker-compose up -d
```

Acesse o navegador no endereço localhost:5000 e siga as instruções em [https://redash.io/help/user-guide/querying](https://redash.io/help/user-guide/querying)