## importando as libs necessárias
import streamlit as st
import pandas as pd
import pickle as pk

## carregando dados e pegando os valores de max e min das váriaveis
df = pd.read_csv("data/casas.csv")

media_area = float(df["tamanho"].mean())
area_max = float(df["tamanho"].max())
area_min = float(df["tamanho"].min())

media_ano = int(df["ano"].mean())
ano_max = int(df["ano"].max())
ano_min = int(df["ano"].min())

## carregando o modelo de ML
with open("models/model_rf.pkl", 'rb') as arquivo:
    modelo_rf = pk.load(arquivo)

## Começando a construção do app 
st.title("Python machine learning app")

st.subheader(
    '''Escolhas as opções abaixo pra realizar a predição'''
)

area = st.slider("qual a área do imóvel", min_value=area_min, max_value=area_max, value=media_area)   

garagem_options = [1, 2, 3]
garagem = st.radio("qual o número de garagens", options=garagem_options)


bairro = st.text_input("informe seu bairro")

ano = st.slider("qual o ano de construção do imóvel", min_value=ano_min, max_value=ano_max, value=media_ano)   


st.sidebar.title("Coloque suas informações")
name_user = st.sidebar.text_input("Digite seu nome")

dados = {
    'tamanho': [area],
    'ano': [ano],
    'garagem': [garagem]
}

click = st.button("Fazer previsão")
if click:
    y_pred = float(modelo_rf.predict(pd.DataFrame(dados))[0])
    y_pred = round(y_pred, 2)
    st.write(f"Olá {name_user} do bairro {bairro}, com as infos passadas o valor da casa é de ${y_pred}")








