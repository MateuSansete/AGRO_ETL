import pandas as pd
import requests
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv() 

# 1. Configurações Globais

# Credenciais do DB
DB_USER = os.getenv('POSTGRES_USER')
DB_PASSWORD = os.getenv('POSTGRES_PASSWORD')
DB_NAME = os.getenv('POSTGRES_DB')
DB_HOST = os.getenv('POSTGRES_HOST')
DB_PORT = os.getenv('POSTGRES_PORT')
TABLE_NAME = 'agriculture_yield'

# Configurações da API Climática
API_KEY = os.getenv('OPENWEATHER_API_KEY')
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?" 

# Exemplo de locais — adapte para a granularidade dos seus dados (município, estado, região etc.).
LOCATIONS = [
    {"city": "Sao Paulo", "country": "BR"},
    {"city": "Minas Gerais", "country": "BR"},
    {"city": "Rio Grande do Sul", "country": "BR"}
]


# 2. Extract - Coleta de Dados Climáticos via API
def extract_weather_data(locations):
    """Obtem dados climáticos via OpenWeatherMap para cada local na lista.

    Retorna um DataFrame com temperatura, umidade, descrição do tempo e carimbo de extração.
    """
    weather_data = []
    print("Extraindo dados climáticos...")
    
    for loc in locations:
        city = loc['city']
        country = loc['country']
        
        # Parâmetros da requisição HTTP
        url = f"{BASE_URL}q={city},{country}&appid={API_KEY}&units=metric"
        
        try:
            response = requests.get(url)
            response.raise_for_status() # Lança exceção para erros HTTP (4xx ou 5xx)
            data = response.json()
            
            # Campos relevantes extraídos da resposta
            record = {
                'city': city,
                'country': country,
                'current_temp_c': data['main']['temp'],
                'humidity_percent': data['main']['humidity'],
                'weather_description': data['weather'][0]['description'],
                'extraction_date': pd.Timestamp.now()
            }
            weather_data.append(record)
            print(f"  Dados de {city} coletados.")
            
        except requests.exceptions.RequestException as e:
            print(f"  Erro ao extrair dados de {city}: {e}")
            
    return pd.DataFrame(weather_data)

# 3. Extract - (Opcional) Leitura de Rendimento Agrícola (CSV estático)
def extract_yield_data(file_path='data/raw/yield_data.csv'):
    """Lê CSV de rendimento agrícola (caminho padrão: data/raw/yield_data.csv)."""
    try:
        df = pd.read_csv(file_path)
        print(f"Rendimento extraído: {len(df)} registros.")
        return df
    except FileNotFoundError:
        print("Arquivo yield_data.csv não encontrado. Retornando DataFrame vazio.")
        return pd.DataFrame()


# 4. Transform - Limpeza e Enriquecimento (O ponto chave)
def transform_data(df_yield, df_weather):
    """Limpa e prepara os dados para carregamento.

    Atualmente aplica limpeza básica ao dataset de rendimento e retorna
    ambos os DataFrames (rendimento e clima) para carga em tabelas separadas.
    """
    print("Transformando dados...")

    # Limpeza: remove registros sem rendimento ou sem ano
    df_yield.dropna(subset=['yield_kg_ha', 'year'], inplace=True)
    df_yield['year'] = df_yield['year'].astype(int)

    # Enriquecimento/merge: placeholder — fazer o cruzamento adequado conforme o modelo
    # de domínio (safra, região, período) quando tiver os identificadores corretos.

    print(f"Transformação concluída. {len(df_yield)} linhas prontas para carga.")
    return df_yield, df_weather


# 5. Load - Carregamento para o PostgreSQL

def load_data(df, table_name):
    """Carrega um DataFrame para o PostgreSQL."""
    db_url = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    engine = create_engine(db_url)
    print(f"Carregando tabela '{table_name}'...")
    
    try:
        # if_exists='append' mantém comportamento incremental
        df.to_sql(table_name, engine, if_exists='append', index=False)
        print(f"Carga de '{table_name}' concluída.")
    except Exception as e:
        print(f"Erro ao carregar '{table_name}': {e}")

# 6. Pipeline Principal
def run_etl():
    # Extração
    df_yield_raw = extract_yield_data() # Dados estáticos de rendimento
    df_weather_raw = extract_weather_data(LOCATIONS) # Dados dinâmicos da API
    
    # Transformação
    df_yield_transformed, df_weather_transformed = transform_data(df_yield_raw, df_weather_raw)
    
    # Carregamento (Load)
    # 1. Carrega dados de Rendimento (Tabela principal)
    load_data(df_yield_transformed, 'yield_records')

    # 2. Carrega dados climáticos (tabela de staging)
    load_data(df_weather_transformed, 'current_weather_data')

    print("\n Pipeline concluído")

if __name__ == "__main__":
    run_etl()