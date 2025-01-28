import pandas as pd
import streamlit as st
from pymongo.mongo_client import MongoClient
import uuid

st.set_page_config(page_title="Your Profile", page_icon=":cat:")
st.sidebar.success("You selected the Profile Page")
st.title("Profile")


@st.cache_resource
def connect_to_mongo():
    #load the user & db password from the secrets.toml file
    user = st.secrets["db_username"]
    db_password = st.secrets["db_password"]

    # This is our database connection string, for a cluster called tb-ii
    uri = f"mongodb+srv://{user}:{db_password}@tb-ii.bluas.mongodb.net/?retryWrites=true&w=majority&appName=tb-ii"

    # Create a new client
    client = MongoClient(uri)
    return client

# Connect to Mongo DB
client = connect_to_mongo()

try:
    client.admin.command('ping')  # Ping-Befehl an MongoDB
    st.success("Verbindung zu MongoDB erfolgreich!")
except Exception as e:
    st.error(f"Verbindung zu MongoDB fehlgeschlagen: {e}")

# Create an empty container
placeholder = st.empty()

# Database & collection name
db_name = "tb-ii"
collection_name = "cat_data"

db = client[db_name]
collection = db[collection_name]

# create a form to collect information
unique_key = str(uuid.uuid4())  # generate an unambiguous ID
with placeholder.form("registration_form"):
    st.subheader("Register user")
    first_name = st.text_input("Enter Your First Name")
    last_name = st.text_input("Enter Your Last Name")
    email = st.text_input("Enter E-Mail*")
    cat_name = st.text_input("Enter Your Cat's Name")
    age = st.number_input("Enter Your Cat's Age (in month)", step=1)
    user_name = st.text_input("Enter User Name*")
    password = st.text_input("Enter User Password*", type="password") #type adds an eye
    repeat_password = st.text_input("Repeat User Password*", type="password")
    submit_button = st.form_submit_button("Register")


# when user clicks on submit button, delete all widgets
if submit_button:
    #define where we want to read and write this data
    db_name = 'tb-ii'
    collection_name = 'cat_data'

    db = client[db_name]
    collection = db[collection_name]

    #add some validation
    if len(password) <1 and len(user_name) <1:
        st.error("Please Enter A Password And A User Name", icon="🚨")
    elif len (password) <1:
        st.error("Please Enter Your Password", icon="🚨")
    elif len (user_name) <1:
        st.error("Please Enter Your Username", icon="🚨")
    elif password != repeat_password:
        st.error("Passwords do not match", icon="🚨")
    elif len(email) <3:
        st.error("Please Enter Your E-Mail", icon="🚨")
    else:
        document = {
            "user_name": user_name,
            "password": password,
            "first_name": first_name,
            "last_name": last_name,
            "cat_name": cat_name,
            "cat_age": age,
            "email": email,
        }

    collection.insert_one(document)

    # Überprüfe, wie viele Dokumente in der Sammlung sind
    count = collection.count_documents({})
    st.write(f"Anzahl der Dokumente in der Sammlung: {count}")

    # Optional: Ausgabe des zuletzt eingefügten Dokuments
    st.write("Eingefügtes Dokument:", document)


    placeholder.empty()
    st.image("https://as2.ftcdn.net/v2/jpg/05/31/67/91/1000_F_531679184_3VykZEvx3OvHKnLpl3TdaDYWT1hYjvc9.jpg")
    st.success(f"Willkommen, {user_name}! Deine Registrierung war erfolgreich.")

