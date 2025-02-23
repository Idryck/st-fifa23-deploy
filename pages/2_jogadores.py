import streamlit as st
import pandas as pd
from datetime import datetime



if 'data' not in  st.session_state:
    df_data=pd.read_csv('CLEAN_FIFA23_official_data.csv', index_col=0)
    df_data=df_data[df_data['Contract Valid Until'] >= datetime.today().year]
    df_data=df_data[df_data['Value(£)']>0]
    df_data=df_data.sort_values(by='Overall', ascending=False)
    st.session_state['data']=df_data
    
    
    
    
md=st.markdown
st.set_page_config(layout='wide', page_title='FIFA23')
#sidebar
#definindo os times
#---------------------------------------
df_data= st.session_state['data']

times= df_data['Club'].value_counts().index
time=st.sidebar.selectbox('Times', times)
#-----------------------------------------------
#definindo os jogadores
df_jogadores=df_data[(df_data['Club']==time)]

jogadores= df_jogadores['Name'].value_counts().index
player=st.sidebar.selectbox ('Jogadores',jogadores)
#------------------------------

#tela
#--------------------------------------------
player_stats=df_data[df_data['Name']==player].iloc[0]

st.title (player_stats['Name'])
st.image(player_stats['Photo'])

md(f""" **Clube:** {player_stats['Club']}\n
   **Posição** {player_stats['Position']}""")
col1, col2, col3, col4= st.columns(4)

col1.markdown(f'**Idade** {player_stats['Age']}')
col2.markdown(f'**Altura** {player_stats['Height(cm.)']/100}')
col3.markdown(f'**Peso** {player_stats['Weight(lbs.)']* 0.453:.2f}')
st.divider()
st.subheader(f'Overal {player_stats['Overall']}')
st.progress(int (player_stats['Overall']))
st.divider()
coll1, coll2, coll3, coll4= st.columns(4)

coll1.metric(label='Valor de Mercado', value= f'£ {player_stats['Value(£)']:,}')
coll2.metric (label='Remuneração Semanal', value=f'£ {player_stats['Wage(£)']:,}')
coll3.metric(label= 'Clausula de Recisão', value=f' £ {player_stats['Release Clause(£)']:,}')
st.divider()