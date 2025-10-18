-- Tabela principal para os dados de Rendimento Agrícola
CREATE TABLE IF NOT EXISTS yield_records (
    id SERIAL PRIMARY KEY,
    crop VARCHAR(100) NOT NULL,
    year INTEGER NOT NULL,
    state VARCHAR(50) NOT NULL,
    yield_kg_ha NUMERIC,
    
    -- Colunas para dados históricos de clima
    avg_temp_c_historical NUMERIC, 
    rainfall_mm_historical NUMERIC,
    
    load_timestamp TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Tabela para os dados Climáticos Coletados da API
CREATE TABLE IF NOT EXISTS current_weather_data (
    id SERIAL PRIMARY KEY,
    city VARCHAR(100) NOT NULL,
    country VARCHAR(2) NOT NULL,
    current_temp_c NUMERIC,
    humidity_percent INTEGER,
    weather_description TEXT,
    extraction_date TIMESTAMP WITHOUT TIME ZONE,
    load_timestamp TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP
);