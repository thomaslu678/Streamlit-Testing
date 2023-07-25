import streamlit as st
from multiapp import MultiApp
from apps import home, about

main = MultiApp()

st.markdown(
    """
    Multi-page App!
    """
)

main.add_app("Home", home.app)
main.add_app("App", about.app)

main.run()