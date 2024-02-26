import streamlit as st
import pandas as pd

def main():
    st.title("Selecione os indicadores de dados que se relacionam com o aprendizado em seu jogo")


    with st.container(border=True):

        df = pd.read_csv('indicadores.csv')

        df = df['Categoria;Indicador'].str.split(';', expand=True)

        df.columns = ['Categoria', 'Indicador']

        categorias_vistas = set()
        x = 0

        agree = []

        if 'key' not in st.session_state:
            st.session_state['key'] = []

        for i in range (len(df['Indicador'])):

            categoria = df['Categoria'][i]
            indicador = df['Indicador'][i]

            # Verificar se a categoria já foi vista antes
            if categoria not in categorias_vistas:
                if x > 0:
                    st.markdown("---")
                st.markdown(f"## {categoria}")
                categorias_vistas.add(categoria)
                x = x + 1
        
            if(st.checkbox(indicador, key=f"{categoria}_{indicador}")):
                agree.append(indicador)
            else:
                # Remover o indicador da lista se o checkbox for desmarcado
                if indicador in st.session_state.key:
                    st.session_state.key.remove(indicador)

    for ind in agree:
        st.session_state.key.append(ind)

    st.markdown(f"## Indicadores selecionados: {len(agree)}")

    st.page_link("pages/resultado.py", label="ENVIAR")


    

    
    


if __name__ == "__main__":
    main()
