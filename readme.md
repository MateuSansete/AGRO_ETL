# Projeto ETL de Rendimento Agrícola 

Este projeto implementa um **pipeline ETL** que processa dados de rendimento de safras agrícolas, com possibilidade de integração de dados climáticos, e carrega os resultados em um **banco de dados PostgreSQL**. O objetivo é permitir análises históricas e correlação entre rendimento e variáveis ambientais.

---

## Tecnologias utilizadas

| Categoria | Ferramenta | Uso no Projeto |
| :--- | :--- | :--- |
| **Pipeline** | **Python 3** | Orquestração, Lógica ETL e Integração com API (`requests`). |
| **Transformação** | **Pandas / NumPy** | Limpeza, padronização e enriquecimento de dados. |
| **Data Warehouse** | **PostgreSQL** | Armazenamento relacional final (`yield_records` e `current_weather_data`). |
| **Conectividade** | **SQLAlchemy / `psycopg2`** | Conexão segura entre Python e PostgreSQL. |
| **Ambiente** | **Docker / Docker Compose** | Containerização completa do DB, ETL e Ambiente de Análise. |
| **Análise** | **Jupyter Notebook** | Análise Exploratória de Dados (EDA) e Visualização. |
| **Integração** | **OpenWeatherMap API** | Fonte de dados climáticos em tempo real. |

---

##  Estrutura do projeto

```
AGRO_ETL/
│── data/
│   └── raw/
│       └── yield_data.csv        # Dados históricos de rendimento (Input primário)
│── notebooks/
│   └── analysis.ipynb           # Script de conexão e Análise Exploratória (EDA)
│── .env.example                 # Exemplo de variáveis de ambiente (Credenciais e API Key)
│── .env                         # Arquivo com as credenciais reais (ignorado pelo Git)
│── docker-compose.yml           # Define os serviços 'postgres', 'pgadmin' e 'etl_runner'
│── Dockerfile                   # Constrói o ambiente Python/Jupyter/Pandas
│── schema.sql                   # Script para criar tabelas no PostgreSQL
│── requirements.txt             # Dependências Python
│── ETL_pipeline.py             # O script principal do pipeline (Extração API + Load)
│── README.md
```



---

## Como rodar o projeto

```bash
### 1. Clone o repositório
git clone https://github.com/MateuSansete/AGRO_ETL.git
cd AGRO_ETL


## 2. Crie e configure o ambiente

- cp .env.example .env  # edite se desejar usuário, senha ou porta do PostgreSQL
- python3 -m venv venv
- source venv/bin/activate
- pip install -r requirements.txt


## 3. Suba os containers do Docker

 
docker-compose up -d
docker-compose ps   

### 1. Preparação e Credenciais
Você deve criar o CSV de dados primários e obter a chave de API.

1.  **Crie a estrutura `data/raw/`** e insira o arquivo `yield_data.csv` (com as colunas: `crop`, `year`, `state`, `yield_kg_ha`, etc.).

2.  **Obtenha uma Chave de API** gratuita na [OpenWeatherMap](https://openweathermap.org/api).

3.  Copie o arquivo de exemplo e preencha as credenciais, incluindo sua `OPENWEATHER_API_KEY`:

## 4. Execute o ETL

python etl/etl_pipeline.py

## 5. Analise os dados

jupyter notebook
Abra o arquivo notebooks/analysis.ipynb.

## 6. (Opcional) Acesse o pgAdmin
URL: http://localhost:8080

Login: admin@admin.com

Senha: admin

Conecte ao PostgreSQL com os dados do arquivo .env.





##  Exemplo de Visualização
Após rodar o notebook, é possível gerar gráficos como este:
[Seu gráfico aqui]

## Status do Projeto
- Em desenvolvimento – 

##  Autor
 [@MateuSansete](https://github.com/MateuSansete)
-->








