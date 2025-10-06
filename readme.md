# Projeto ETL de Rendimento Agrícola 

Este projeto implementa um **pipeline ETL** que processa dados de rendimento de safras agrícolas, com possibilidade de integração de dados climáticos, e carrega os resultados em um **banco de dados PostgreSQL**. O objetivo é permitir análises históricas e correlação entre rendimento e variáveis ambientais.

---

## Tecnologias utilizadas

- **Python 3** – pipeline e análises
- **Pandas / NumPy** – manipulação de dados
- **PostgreSQL** – banco relacional
- **SQLAlchemy / psycopg2** – conexão Python ↔ PostgreSQL
- **Docker / Docker Compose** – containerização do banco e serviços
- **Jupyter Notebook** – análise exploratória e gráficos
- **Matplotlib / Plotly** – visualização de dados
- **Prefect / Airflow (opcional)** – orquestração de pipelines

---

##  Estrutura do projeto

agriculture_yield_project/
│── etl/
│ └── etl_pipeline.py
│── notebooks/
│ └── analysis.ipynb
│── docker-compose.yml
│── schema.sql
│── requirements.txt
│── .env.example
│── data/
│ ├── raw/
│ └── processed/
│── README.md

yaml
Copiar código

---

---

## Como rodar o projeto

### 1. Clone o repositório
```bash
git clone https://github.com/MateuSansete/AGRO_ETL.git
cd AGRO_ETL


## 2. Crie e configure o ambiente

- cp .env.example .env  # edite se desejar usuário, senha ou porta do PostgreSQL
- python3 -m venv venv
- source venv/bin/activate
- pip install -r requirements.txt


## 3. Suba os containers do Docker

 
docker-compose up -d
docker-compose ps   # verificar se postgres e pgadmin subiram


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



Exemplo de Visualização
Após rodar o notebook, é possível gerar gráficos como este:


> Status do Projeto
- Em desenvolvimento – contribuições são bem-vindas.

Autor
Feito por Mateus Bastos @MateuSansete








