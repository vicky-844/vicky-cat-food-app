import streamlit as st
import random
import requests

st.set_page_config(page_title="Chill Music",
                   page_icon=":music:")

st.title("Majestic Chill Lounge")
st.write("Sit back and relax with relaxing cat music. Simply play and enjoy!")

#relaxing music
st.subheader("DJ Booth")

video_list = [
    "https://www.youtube.com/watch?v=dN8MQpcW_P4&pp=ygUPY2hpbGwgY2F0IG11c2lj",
    "https://www.youtube.com/watch?v=wn0IyvGBeUI",
    "https://www.youtube.com/watch?v=vvThzcBfnyc&pp=ygUObG9maSBjYXQgbXVzaWM%3D",
    "https://www.youtube.com/watch?v=sR6tjNq8Ywk&pp=ygUObG9maSBjYXQgbXVzaWM%3D",
    "https://www.youtube.com/watch?v=GBz5_IvngL8&pp=ygUObG9maSBjYXQgbXVzaWM%3D",
    "https://www.youtube.com/watch?v=TFpaqmAZoAY&pp=ygUObG9maSBjYXQgbXVzaWM%3D",
]

#play random yt-video
random_video = random.choice(video_list)
st.video(random_video)

st.divider()

#random cat gifs from The Cat API
st.subheader("Funny Cat-GIF")
url = "https://api.thecatapi.com/v1/images/search?mime_types=gif"

#request to API
response = requests.get(url)

#extract GIF
gif_url = response.json()[0]['url']

#show GIF
st.image(gif_url)

