import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

# Conexão com o banco local SQLite
engine = create_engine('sqlite:///iot_db.db')

# Função para carregar dados das Views SQL
def load_data(view_name):
    return pd.read_sql(f"SELECT * FROM {view_name}", engine)

# Layout do Dashboard
st.set_page_config(page_title="IoT Dashboard", layout="wide")
st.title('🌡️ Dashboard de Temperaturas IoT')
st.write("Pipeline de Dados com Processamento SQL, SQLAlchemy e Visualização Interativa")
st.divider()

col1, col2 = st.columns(2)

# Gráfico 1
with col1:
    st.subheader('Média de Temperatura por Local')
    df_avg_temp = load_data('avg_temp_por_dispositivo')
    fig1 = px.bar(df_avg_temp, x='device_id', y='avg_temp', color='device_id',
                  labels={'device_id': 'Local (In/Out)', 'avg_temp': 'Temperatura Média (°C)'})
    st.plotly_chart(fig1, use_container_width=True)

# Gráfico 2
with col2:
    st.subheader('Volume de Leituras por Hora do Dia')
    df_leituras_hora = load_data('leituras_por_hora')
    fig2 = px.line(df_leituras_hora, x='hora', y='contagem', markers=True,
                   labels={'hora': 'Hora do Dia', 'contagem': 'Qtd de Leituras'})
    st.plotly_chart(fig2, use_container_width=True)

# Gráfico 3
st.subheader('Temperaturas Máximas e Mínimas Diárias')
df_temp_max_min = load_data('temp_max_min_por_dia')
fig3 = px.line(df_temp_max_min, x='data', y=['temp_max', 'temp_min'], markers=True,
               labels={'data': 'Data', 'value': 'Temperatura (°C)', 'variable': 'Métrica'})
st.plotly_chart(fig3, use_container_width=True)