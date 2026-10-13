import pandas as pd
from sqlalchemy import create_engine, text

# 1. Conexão com o banco local SQLite (cria o ficheiro iot_db.db na raiz)
engine = create_engine('sqlite:///iot_db.db')

print("Lendo o arquivo CSV...")
df = pd.read_csv('data/IOT-temp.csv')

# Renomeia colunas removendo barras e caracteres especiais
df.columns = ['id', 'room_id', 'noted_date', 'temp', 'out_in']

# Converte a coluna de data
df['noted_date'] = pd.to_datetime(df['noted_date'], format='%d-%m-%Y %H:%M', errors='coerce')

print("Enviando dados para o banco SQLite local...")
df.to_sql('temperature_readings', engine, if_exists='replace', index=False)

print("Criando as 3 Views SQL exigidas...")
with engine.connect() as conn:
    # View 1: Média por local
    conn.execute(text("""
    CREATE VIEW IF NOT EXISTS avg_temp_por_dispositivo AS
    SELECT out_in AS device_id, AVG(temp) as avg_temp
    FROM temperature_readings
    GROUP BY out_in;
    """))
    
    # View 2: Leituras por hora (no SQLite usamos strftime para extrair a hora)
    conn.execute(text("""
    CREATE VIEW IF NOT EXISTS leituras_por_hora AS
    SELECT strftime('%H', noted_date) AS hora, COUNT(*) AS contagem
    FROM temperature_readings
    WHERE noted_date IS NOT NULL
    GROUP BY hora
    ORDER BY hora;
    """))
    
    # View 3: Máxima e mínima por dia
    conn.execute(text("""
    CREATE VIEW IF NOT EXISTS temp_max_min_por_dia AS
    SELECT DATE(noted_date) AS data, MAX(temp) AS temp_max, MIN(temp) AS temp_min
    FROM temperature_readings
    WHERE noted_date IS NOT NULL
    GROUP BY data
    ORDER BY data;
    """))
    conn.commit()

print("Sucesso! Banco alimentado e views criadas.")