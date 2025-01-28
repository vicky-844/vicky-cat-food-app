import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd

#resources for homepage
#.streamlit blog => multipage blog: https://blog.streamlit.io/introducing-multipage-apps/
#               =>                 https://www.youtube.com/watch?v=oqo8-1c4H-k
#dataframe .streamlit => https://docs.streamlit.io/develop/api-reference/data/st.dataframe?ref=blog.streamlit.io
#create different pages => https://www.youtube.com/watch?v=YClmpnpszq8

#setting up homepage
st.set_page_config(page_title="Majastic Food",
                   page_icon=":cat:")
#st.sidebar.success("Select a majastic page above")
st.title("WELCOME TO MAJASTIC FOOD")

with st.sidebar:
    selected = option_menu(
        menu_title="Navigation",  # Titel der Navigation
        options=["Startseite", "Katzenfutter-Finder", "Ernährungs-Ratgeber", "Profilseite"],  # Seiten
        icons=["house", "search", "book", "person"],  # Optionale Icons
        menu_icon="menu-app",  # Icon für das Menü
        default_index=0,  # Startseite als Standard
    )


#goal of App = best nutrition for your senior cat !

#Brief information on the importance of nutrition for older cats (e.g. kidney-friendly, protein requirements, etc.).

#Tips on how users can best use the app!