# 🌡️ Pipeline de Dados com IoT e Docker

Projeto prático desenvolvido para a disciplina de **Disruptive Architectures: IoT, Big Data e IA** do curso de Análise e Desenvolvimento de Sistemas da UniFECAF.

## 🎯 Objetivo do Projeto
Desenvolver um pipeline completo de engenharia de dados com foco em dispositivos IoT. O sistema processa um dataset massivo de leituras de temperatura, estrutura essas informações em um banco de dados relacional e as disponibiliza através de um dashboard analítico interativo, permitindo análises críticas sobre o comportamento térmico de ambientes internos e externos.

## 🛠️ Tecnologias Utilizadas
*   **Python:** Linguagem principal para construção do script de ETL (processamento de dados) e da aplicação web.
*   **Pandas:** Tratamento, higienização e conversão de tipos dos dados recebidos via CSV.
*   **PostgreSQL / SQLite:** Armazenamento relacional estruturado dos dados das leituras IoT. *(O código suporta ambos os motores via SQLAlchemy)*.
*   **Docker:** Orquestração do banco de dados (Container PostgreSQL), garantindo isolamento de infraestrutura.
*   **Streamlit:** Framework para a criação do dashboard interativo.
*   **Plotly Express:** Geração de gráficos e visualizações ricas no front-end.
*   **Git/GitHub:** Controle de versionamento e repositório de entrega.

## ⚙️ Instruções de Execução (Passo a Passo)

### 1. Pré-requisitos
*   Python 3.10 ou superior.
*   Docker Desktop (Opcional, caso utilize o PostgreSQL).
*   Baixe o dataset `IOT-temp.csv` no [Kaggle](https://www.kaggle.com/datasets/atulanandjha/temperature-readings-iot-devices) e coloque dentro da pasta `data/`.

### 2. Configuração do Ambiente Virtual e Dependências
Abra o terminal na raiz do projeto e execute:
```bash
# Cria o ambiente virtual
python -m venv venv

# Ativa o ambiente virtual (Windows)
.\venv\Scripts\activate

# Instala as dependências necessárias
pip install -r requirements.txt