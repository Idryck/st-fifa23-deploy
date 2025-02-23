import streamlit as st
import webbrowser as wb
import pandas as pd
from datetime import datetime

if 'data' not in  st.session_state:
    df_data=pd.read_csv('CLEAN_FIFA23_official_data.csv', index_col=0)
    df_data=df_data[df_data['Contract Valid Until'] >= datetime.today().year]
    df_data=df_data[df_data['Value(£)']>0]
    df_data=df_data.sort_values(by='Overall', ascending=False)
    st.session_state['data']=df_data
md=st.markdown
md('# Dataset oficial FIFA 2023! ')
btn=st.link_button('Disponivel em:', 'https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data')


st.sidebar.markdown ("Analise Desenvolvida por [Lucas Souza](https://www.linkedin.com/in/lucas-souza-470365351/)")

md(''' O dataset disponível no Kaggle sobre o FIFA 23 é uma excelente fonte de dados para entusiastas de futebol, cientistas de dados e desenvolvedores que desejam explorar informações detalhadas sobre jogadores, times, ligas e características do jogo. Ele contém uma vasta gama de atributos que refletem as habilidades, estatísticas e informações pessoais dos jogadores, bem como dados relacionados aos clubes e competições.

Principais Características do Dataset:
Dados dos Jogadores:

Informações Básicas: Nome, idade, nacionalidade, clube atual, posição, pé dominante, etc.

Habilidades e Estatísticas: Avaliações de habilidades como dribling, finalização, passe, defesa, velocidade, força física, entre outras.

Potencial e Valor de Mercado: Potencial de crescimento do jogador e seu valor de mercado estimado.

Características Especiais: Habilidades únicas, como "Chute de Trivela", "Visão de Jogo", "Marcação Pressão", etc.

Dados dos Clubes:

Nome do clube, liga em que disputa, orçamento, valor total do elenco e reputação.

Informações sobre estádios, como capacidade e nome.

Dados das Ligas e Competições:

Lista de ligas disponíveis no FIFA 23, com detalhes sobre os times participantes e o nível de competitividade.

Atributos Físicos e Técnicos:

Altura, peso, overall (avaliação geral), potencial, salário e duração do contrato.

Detalhes técnicos como precisão de passe, controle de bola, agilidade, equilíbrio e muito mais.

Dados Adicionais:

Fotos dos jogadores (quando disponíveis).

Informações sobre lesões e características especiais, como "Talentos Jovens" ou "Lendas do Jogo".''')