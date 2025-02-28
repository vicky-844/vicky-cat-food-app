import streamlit as st
import random

st.set_page_config(page_title="About Majastic Food",
                   page_icon=":cat:")


#picture of maja
image_path = "pages/about_maja.JPG"
st.image("pages/about_maja.JPG", caption="Majestic Food Mastermind", use_container_width=True)

st.title("About Majastic Food")


#introduction
st.write("### Hello Everyone 👋")
st.write(
    "I'm **Maja**, 9 years old and owner of the human who made this application for me. "
    "You could call me the inspiration and therefore the mastermind behind all of this!"
)

st.divider()

#hobbies
st.write("### My Hobbies")
st.write(
    "- **Sleeping** 💤\n"
    "- **Eating** 🍽️\n"
    "- **Keeping humans in check** 😼\n"
)

#character description
st.write(
    "I may look super cute on the outside, but I rarely let myself be cuddled. "
    "Sometimes a massage is nice, but then these humans suddenly get super clingy and want to cuddle - ugh! "
    "In such cases, I like to get my claws out and show them who's in charge! 😼"
)

st.divider()

fun_facts = [
    "Maja sleeps about 16 hours a day! 😴",
    "Maja loves to test food - but only the best! 🍗",
    "Maja only tolerates cuddling when she wants it! 🐈",
    "Maja has trained her humans perfectly. 😉",
    "Maja is night-active and likes to play when all her servants are asleep. 🎇"
]

if st.button("Click for a Fun Fact about Maja!"):
    st.write(random.choice(fun_facts))

st.divider()

#nutrition
st.write("### Food & Nutrition")
st.write(
    "Even if my servants at home still see me as a baby, at 9 years old I am already a **senior cat**. "
    "This means that age-appropriate nutrition is particularly important! "
    "My servants have a hard time because of this – there is comparatively less senior cat food than for other age groups, "
    "and of course, I have a very **sophisticated taste** and am quite picky about food! 😼🍽️"
)

#app explaination
st.write(
    "With the help of this app, you can check **over 70 different cat foods** and see which product "
    "has the most important analytical nutrients. "
    "If you are interested in more information, please click on **“Information”** in the menu!"
)


st.write("### Bon Appetit! 🍴")
st.write("**- Maja and her servant**")

