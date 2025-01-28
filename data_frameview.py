import streamlit as st
import pandas as pd
import streamlit_pandas as sp

st.set_page_config(page_title="Dataframe")
st.title("Majastic Database")
st.text("With this application you can filter out cat food, fitting best to your furry majesty! ")

#insert excel spreadsheet -> tutorial: https://www.youtube.com/watch?v=7E3yxq-P-a8
def load_data():
    df = pd.read_excel("cat_food_overview.xlsx")
    return df

df = load_data()
    
#querying data from spreadsheet -> https://www.youtube.com/watch?v=L4KVn1XnSAA
all_widgets = sp.create_widgets(df)
res = sp.filter_df(df, all_widgets)
st.write(res)



st.dataframe(df)

