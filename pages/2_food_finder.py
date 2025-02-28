import streamlit as st
import pandas as pd
import random
import os

st.set_page_config(page_title="Food Finder")
st.title("Majestic Food Finder🐾")

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
    if os.path.exists("cat_food_overview.xlsx"):
        df = pd.read_excel("cat_food_overview.xlsx")
        st.success("Excel file loaded successfully!")
        return df
    else:
        st.error("Excel file not found!")
        return pd.DataFrame()  # return empty if error

df = load_data()

#top 5 cat food
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

selected_columns = ["Brand", "Name", "Sort", "Protein", "Fat", "Raw Ashes", "Raw Fiber", "Moisture", "Phosphorus", "Sodium", "Drink Water", "prod. In Germany?"]


filters = {}

# Sidebar Filter (for categorical columns)
for col in selected_columns:
    if col in df.columns:
        if df[col].dtype == 'object':  #for text
            unique_values = df[col].dropna().unique()
            selected_values = st.sidebar.multiselect(f"Select values for {col}", unique_values)
            if selected_values:
                filters[col] = selected_values
        elif df[col].dtype in ['float64', 'int64']:  #for numeric data
            min_value = df[col].min()
            max_value = df[col].max()
            selected_range = st.sidebar.slider(
                f"Select range for {col}", min_value, max_value, (min_value, max_value)
            )
            filters[col] = selected_range

filtered_df = df.copy()

# Apply the filters to the dataframe
for col, values in filters.items():
    if isinstance(values, tuple):  # Numerischer Bereich (für Slider)
        filtered_df = filtered_df[(filtered_df[col] >= values[0]) & (filtered_df[col] <= values[1])]
    else:  # Textwerte (für Multiselect)
        filtered_df = filtered_df[filtered_df[col].isin(values)]

st.write(filtered_df)

st.success("Tip: Senior cats need **high protein** and **low phosphorus** food to prevent kidney disease! 🩺🐱")

if st.button("🎲 Give me a random food recommendation!"):
    if not df.empty:  # Sicherstellen, dass DataFrame nicht leer ist
        random_food = df.sample(1)  # Zufällige Zeile aus DataFrame
        st.write(random_food)
    else:
        st.error("No data available, please check the Excel file.")
