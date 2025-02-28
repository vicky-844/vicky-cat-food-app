import streamlit as st
import random

st.set_page_config(page_title="Information",
                   page_icon="💡")
st.title("Good To Know 💡")
st.divider()
st.image("https://images.unsplash.com/photo-1597843786411-a7fa8ad44a95?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D")
st.divider()

st.subheader("Important facts about the nutrition of senior cats! ")
st.write(
    "Cat food is a broad topic - there is an enormous selection in supermarkets, pet shops and online, which often makes it difficult for cat owners to find the right food. "
    "In 2016 alone, specialist retailers generated sales of over 1.6 billion euros with cat food. "
    "The majority of this was accounted for by wet food, with sales of around 1.07 billion euros, followed by dry food and snacks."
    "But how do you find the best food for your cat, especially for older cats who have different needs? "
)
st.write("Here are some points to look out for when choosing. But remember - this summary should provide an initial overview,"
         "and is not a substitute for a consultation with your vet!")


st.divider()
st.image("https://images.unsplash.com/photo-1616240133571-146fa869b7ce?q=80&w=2072&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D")
st.divider()
st.subheader("Wet food or dry food: which is better for your cat?")
st.write(
    "**Cats are natural carnivores** and meet their fluid requirements mainly through food. "
    "As they are naturally lazy drinkers, **wet food** is the better choice. "
    "It accommodates the cat's natural behavior and helps to avoid dehydration, which can put a strain on the kidneys in particular. "
    "In comparison, **dry food** cannot adequately cover the cat's fluid requirements and often leads to dehydration. "
    "It also swells up in the stomach, so cats often eat more than they actually need - which can lead to obesity. "
)
st.write("If you still prefer dry food, you should offer your cat several drinking options, such as **drinking fountains** or **fresh water in several bowls**.")


st.divider()
st.image("https://images.unsplash.com/photo-1625793995159-59836c45c2ca?q=80&w=1931&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D")
st.divider()
st.subheader("Understanding cat food declarations")
st.write(
    "If you want to choose the right food for your cat, you need to read the declaration on the packaging carefully. "
    "**Meat should always be the main ingredient in the food.** But what about terms such as “animal by-products”? "
    "These often refer to **leftovers from food production**, such as intestines, bones and other parts of animals that are also eaten by cats in the wild. "
    "A certain proportion of these by-products is therefore normal. "
    "However, it is important to be able to trace how much and which animal ingredients are actually contained in the food. "
    "Animal by-products are often cheaper for manufacturers than high-quality meat and can reduce the quality of the food. "
    "As a rule, cats then need more food to cover the same nutritional requirements."
)


st.divider()
st.image("https://images.unsplash.com/photo-1516784587776-fc6e541046d7?q=80&w=2063&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D")
st.divider()
st.subheader("Plant by-products: Why should they be avoided?")
st.write(
    "Many cat foods contain vegetable by-products such as soy, corn or wheat, which are often used as fillers or to improve the protein content. "
    "However, **cats cannot digest long carbohydrates** from plants, which can damage their health in the long term. "
    "Too much plant-based food can not only trigger allergies, but also put a strain on the organs. "
    "Rice and potatoes are better than plant-based ingredients."
)


st.divider()
st.image("https://images.unsplash.com/photo-1511173452976-d0191e5db96a?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D")
st.divider()
st.subheader("Sugar, coloring and flavor enhancers: What is really necessary?")
st.write(
    "Some cat foods contain sugar, even though cats cannot taste it. "
    "Sugar is often used as a flavor enhancer, but can lead to obesity, plaque and other health problems. "
    "There are also colorings and thickeners that are intended to make the food more attractive, but offer **no health benefits.** "
)


st.divider()
st.image("https://images.unsplash.com/photo-1532303517831-241791b20fb9?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D")
st.divider()
st.subheader("What do the analytical parameters reveal?")
st.write(
    "In addition to the list of ingredients, every cat food package also contains the **analysis values**, which indicate the proportion of protein, fat, fiber and minerals. "
    "These are particularly important:"
    "**Raw protein:** A value between **5-15%** for wet food is ideal. The protein should come from animal sources, as cats can only effectively utilize animal protein."
    "**Raw fat:** A proportion of **5-8%** is good, with animal fats being preferred."
    "**Raw ash:** A value **between 1.5 and 2%** indicates the proportion of minerals. In particular, the ratio of calcium to phosphorus should be around 1.2:1."
    "**Raw fiber:** This value should be as **low as possible** - less than 1% for moist feed."
)


st.divider()
st.image("https://images.unsplash.com/photo-1645773619957-ec1d128d0aa2?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NTl8fGthdHplbmZ1dHRlcnxlbnwwfDB8MHx8fDI%3D")
st.divider()
st.subheader("The right dosage: pay attention to quantity")
st.write(
    "Last but not least, the **dosage** of the food is also crucial. "
    "If a small amount of food is sufficient, this indicates a high nutrient density, which speaks for high-quality food."
    "Cat owners should therefore pay attention to the recommended amount per day."
)


st.divider()

st.write("Depending on what stage of life your cat is in, it will have different nutritional needs. "
         "To prevent possible age-related diseases, it is therefore important to ensure a **low phosphorus content**, a **low sugar content** and a **high-quality of raw meat and liquids**.")




st.divider()
st.image("https://images.unsplash.com/photo-1501820488136-72669149e0d4?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8Y2F0JTIwbXl0aHN8ZW58MHwwfDB8fHwy")
st.divider()


#myth-buster section
st.subheader("Mythbusters: Debunking Myths about Cat Food 🐾")
st.write("Click the button to discover a random myth about senior cat nutrition and its fact-based clarification!")



#list of myths & facts
myths_and_facts = [
    {
        "myth": "Myth 1: Dry food is better for cats’ dental health",
        "fact": "Fact: While kibble is often thought to help clean teeth, studies show it has minimal benefits for plaque and tartar reduction. "
                "In fact, some dry foods are high in carbohydrates, which may lead to obesity. "
                "Wet food provides better hydration and supports overall health. Tooth brushing and professional dental cleanings are key to dental health."
    },

    {
        "myth": "Myth 2: Grain-free diets are better for cats",
        "fact": "Fact: While grain-free diets are popular, cats rarely have specific grain allergies. "
                "Often, grains are replaced with other carbohydrates like potatoes or peas, which can also cause issues. "
                "Focus on a balanced diet with high-quality protein rather than eliminating grains."
    },

    {
        "myth": "Myth 3: Cats can self-regulate their food intake",
        "fact": "Fact: Cats cannot self-regulate their food intake effectively. "
                "If given free access to food, they will often overeat, leading to obesity and related health issues. "
                "Portion control and scheduled feeding are important for a healthy weight."
    },

    {
        "myth": "Myth 4: Homemade or raw diets are healthier",
        "fact": "Fact: Homemade diets can lack essential nutrients and may lead to deficiencies or imbalances. "
                "These diets require careful planning and strict hygiene to avoid contamination. "
                "Consult a veterinary nutritionist before opting for homemade meals for your cat."
    },

    {
        "myth": "Myth 5: Cats can thrive on a vegan or vegetarian diet",
        "fact": "Fact: Cats are obligate carnivores and require animal-based nutrients like taurine and vitamin B12, which are absent in vegan or vegetarian diets. "
                "A plant-based diet can cause serious health issues, such as heart disease and blindness."
    },

    {
        "myth": "Myth 6: Cats love and should drink milk",
        "fact": "Fact: Most adult cats are lactose intolerant and drinking milk can cause digestive upset, including diarrhea. "
                "Always provide fresh water, and consider adding tuna water for a special treat."
    },


    {
        "myth": "Myth 7: Table scraps are safe for cats",
        "fact": "Fact: Many foods we eat, such as onions, garlic, chocolate, and xylitol, are toxic to cats. "
                "Table scraps can also lead to an unbalanced diet, contributing to obesity and health problems. "
                "Stick to quality cat food and cat-friendly treats instead."
    },
]

if st.button('Show Random Myth'):
    myth_fact = random.choice(myths_and_facts)

    #show the selected myth and fact
    st.subheader(myth_fact['myth'])
    st.write(myth_fact['fact'])

#additional information
st.divider()
st.write(
    "These myths are common in cat nutrition, but it's essential to rely on facts to make the best choices for your senior cat's health. "
    "Always consult your vet when in doubt.")