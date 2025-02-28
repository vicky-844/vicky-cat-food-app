import streamlit as st
import requests
import random


#setting up homepage
st.set_page_config(page_title="Majastic Food",
                   page_icon="👑")
st.title("🐾 Majestic Food - The Health App for Your Senior Cats 🐾")
st.divider()


#welcoming
st.markdown(
    """
    ### Hello friends of the furry majesties! 👑🐱  
    **Welcome to Majestic Food!**  
    Your **health app for senior cats**, giving you an **overview of medical records**  
    and helping you find the **best possible cat food** for your majestic cat.
    """
)


st.divider()
#manual
st.info(
    """
    ### How does the app work?  
    🏠 **Navigate easily** using the sidebar menu.  
    👤 **Create a profile** under "Profiles" to track your cat's data.  
    🍽  **Find the perfect food** under "Food Finder" with our smart filter.  
    🧠 **Learn about senior cat nutrition** in "Good to Know". 
    ❤️ **Our goal:** Prevent diseases common in senior cats, such as kidney insufficiency, by providing the right nutrition! 🩺🥩
    
    🚀 **Try it out now and find the best food for your cat!**
    """
)

#random cat fun fact
cat_facts = [
    "Cats sleep for around 13–16 hours a day. 😴",
    "A cat’s nose is as unique as a human fingerprint. 👃",
    "Cats can rotate their ears 180 degrees. 👂",
    "Your cat only meows to communicate with humans – not other cats! 🗣️",
    "The oldest recorded cat lived for 38 years! 🎂",
    "Cats can jump up to six times their body length in one leap! 🏆",
    "A cat’s whiskers are roughly as wide as its body – perfect for sensing spaces! 🐾"
]
random_fact = random.choice(cat_facts)
st.info(f"**Did you know?** 🐱 {random_fact}")

st.divider()


#cat of the day
st.subheader("Cat of the Day📸 ")
try:
    cat_api_url = "https://api.thecatapi.com/v1/images/search"
    response = requests.get(cat_api_url).json()
    cat_image_url = response[0]["url"]
    st.image(cat_image_url, caption="Cat of the Day! 🐱", use_container_width=True, width=50)
except:
    st.warning("Couldn't load today's cat. But don't worry, your own cat is the cutest! 🐾")
