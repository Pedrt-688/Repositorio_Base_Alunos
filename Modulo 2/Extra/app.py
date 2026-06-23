import streamlit as st
st.title("Cristiano RH - Contrata mais que o bobo do Messi")
### colocar imagem
st.sidebar.image("logo.png")
###Acima imagem
nome = st.text_input('Digite o nome do Funcionário: ')
idade= st.text_input('Digite a idade do Funcionário: ')
email= st.text_input('Digite o Email do Funcionário: ')
salario= st.text_input('Digite o Salario do Funcionário: ')
cargo= st.text_input('Digite o Cargo do funcionário: ')

if st.button('Cadastrar'):
    st.warning(f'o funcionário {nome}, foi cadastrado com sucesso')
    st.balloons()

