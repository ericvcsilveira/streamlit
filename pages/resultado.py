import streamlit as st

def main():

    for indicador in st.session_state.key:
        st.write(indicador)

if __name__ == "__main__":
    main()