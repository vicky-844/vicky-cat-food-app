import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="Food Finder")
st.title("Majastic Food Finder🐾")

st.markdown(
    """
    ### Find the perfect food for your furry majesty! 👑🐱  
    Use the filters on the left to find the best cat food for your senior cat.  
    You can filter by brand, name and sort or, if you're interested in the analytical components, by protein, fat, and other essential nutrients.  
    """
)

st.divider()

st.info("We recommend reading the page “Good To Know” to get an overview of the nutrition of senior cats!"
        "However, it is best to discuss the diet with your vet in order to tailor it perfectly to your furry majesty. 👑")

st.divider()



# insert excel spreadsheet -> tutorial: https://www.youtube.com/watch?v=7E3yxq-P-a8
@st.cache_data
def load_data():
    df = pd.read_excel("cat_food_overview.xlsx")
    return df

df = load_data()

#top 3 cat food
def get_top_5_foods(df):
    #make sure data is numeric
    df["Phosphorus"] = pd.to_numeric(df["Phosphorus"], errors="coerce")
    df["Protein"] = pd.to_numeric(df["Protein"], errors="coerce")

    #my own criteria to filter
    filtered_df = df[(df["Phosphorus"] <= 0.02) & (df["Protein"] >= 0.10)]

    top_foods = filtered_df.head(5)

    return top_foods


#button for top 3 recommendations
if st.button("🏆 Show Top 5 Cat Foods"):
    top_5_foods = get_top_5_foods(df)

    if not top_5_foods.empty:
        st.write(top_5_foods)
    else:
        st.warning("No cat food meets the criteria! Try adjusting your filters.")


#if excel is updated run refresh to show changes
#if st.button("Refresh Excel 🔄"):
    #st.cache_data.clear()
    #st.success("Cache cleared! Data has been updated.")

selected_columns = ["Brand", "Name", "Sort", "Protein", "Fat", "Raw Ashes", "Raw Fiber", "Moisture", "Phosphorus", "Sodium", "Drink Water", "prod. In Germany?", "Bio"]

# querying data from spreadsheet -> https://www.youtube.com/watch?v=L4KVn1XnSAA
filters = {}
for col in selected_columns:
    unique_values = df[col].dropna().unique()
    selected_values = st.multiselect(f"Select values for {col}", unique_values)
    if selected_values:
        filters[col] = selected_values

filtered_df = df.copy()
for col, values in filters.items():
    filtered_df = filtered_df[filtered_df[col].isin(values)]

st.write(filtered_df)

st.success("Tip: Senior cats need **high protein** and **low phosphorus** food to prevent kidney disease! 🩺🐱")

if st.button("🎲 Give me a random food recommendation!"):
    random_food = df.sample(1)  # Zufällige Zeile aus DataFrame
    st.write(random_food)
