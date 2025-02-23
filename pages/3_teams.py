import streamlit as st

md=st.markdown
st.set_page_config(layout='wide', page_title='FIFA23')

df_data= st.session_state['data']
times= df_data['Club'].value_counts().index
time=st.sidebar.selectbox('Times', times)

df_filtrado= df_data [(df_data['Club']==time)].set_index('Name')

st.image(df_filtrado.iloc[0]['Club Logo'])

st.title(f" {time}")

columns = ["Age", "Photo", "Flag", "Overall", 'Value(£)', 'Wage(£)', 'Joined', 
           'Height(cm.)', 'Weight(lbs.)',
           'Contract Valid Until', 'Release Clause(£)']

st.dataframe(df_filtrado[columns], column_config={
    "Overall":st.column_config.ProgressColumn(format='%d', min_value=0, max_value=100),
    'Wage(£)':st.column_config.ProgressColumn('ganho semanal', format='%f', min_value=0, max_value=df_filtrado['Wage(£)'].max()),
    "Photo": st.column_config.ImageColumn(),
    "Flag": st.column_config.ImageColumn('País')
})