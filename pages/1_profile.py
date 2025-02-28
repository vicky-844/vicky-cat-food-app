import streamlit as st
from pymongo.mongo_client import MongoClient
import gridfs
from PIL import Image
import io
from datetime import datetime
import fitz
from bson import ObjectId
import time

#page setup
st.set_page_config(page_title="Your Profile", page_icon=":cat:")
st.sidebar.success("You selected the Profile Page")
st.title("Profile 🐾")

#MongoDb connection
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

client = connect_to_mongo()
db_name = "tb-ii"
collection_name = "cat_data"
db = client[db_name]
collection = db[collection_name]

#Set up GridFS
fs = gridfs.GridFS(db)


#feedback connection to Mongo DB
#try:
    #client.admin.command('ping')
    #st.success("Connection to MongoDB successful!")
#except Exception as e:
    #st.error(f"Connection to MongoDB failed: {e}")



#session state login status
if "logged_in_user" not in st.session_state:
    st.session_state.logged_in_user = None
if "auth_selection" not in st.session_state:
    st.session_state.auth_selection = "Login"
if "new_upload" not in st.session_state:
    st.session_state.new_upload = False


#selection login or registration
if not st.session_state.logged_in_user:
    st.session_state.auth_selection = st.selectbox(
        "Would you like to register or log in?",
        ["Login", "Registration"],
        index=0 if st.session_state.auth_selection == "Login" else 1,
        key="auth_selection_main"
    )

    # LOGIN
    if st.session_state.auth_selection == "Login":
        with st.form("login_form"):
            st.subheader("Login")
            user_name = st.text_input("Username")
            password = st.text_input("Password", type="password")
            login_button = st.form_submit_button("Login")

        if login_button:
            user = collection.find_one({"user_name": user_name, "password": password})
            if user:
                st.session_state.logged_in_user = user
                st.success(f"Welcome Back, {user_name}! 🎉")
                st.rerun()
            else:
                st.error("Username or password incorrect!")


    # REGISTRATION
    elif st.session_state.auth_selection == "Registration":
        with st.form("registration_form"):
            st.subheader("Register User")
            first_name = st.text_input("Enter Your First Name")
            last_name = st.text_input("Enter Your Last Name")
            email = st.text_input("Enter E-Mail*")
            cat_name = st.text_input("Enter Your Cat's Name")
            cat_birthdate = st.date_input("Enter Your Cat's Birthdate")
            user_name = st.text_input("Enter User Name*")
            password = st.text_input("Enter User Password*", type="password")
            repeat_password = st.text_input("Repeat User Password*", type="password")
            submit_button = st.form_submit_button("Register")

        if submit_button:
            if not user_name or not password:
                st.error("Please enter a username and password! 🚨")
            elif password != repeat_password:
                st.error("Passwords do not match! 🚨")
            elif collection.find_one({"user_name": user_name}):
                st.error("Username already exists! 🚨")
            elif len(email) < 3:
                st.error("Please enter a valid email address! 🚨")
            else:
                document = {
                    "user_name": user_name,
                    "password": password,
                    "first_name": first_name,
                    "last_name": last_name,
                    "email": email,
                    "cat_name": cat_name,
                    "cat_birthdate": str(cat_birthdate),
                    "cat_weight": 0,  # Default value
                    "cat_breed": "Unknown",  # Default value
                }
                collection.insert_one(document)
                st.success(f"Registration successful! Welcome, {user_name}. Please log in.")
                time.sleep(3)
                st.session_state["registration_successful"] = True
                st.rerun()


# PROFILE PAGE
else:
    user = collection.find_one({"user_name": st.session_state.logged_in_user["user_name"]})
    st.session_state.logged_in_user = user
    st.success(f"Welcome, {user['user_name']}! 🎉")

    col1, col2 = st.columns([1, 1])

    with col1:
        st.subheader("Your Profile Picture 📷")
        if "profile_image_id" in user and user["profile_image_id"]:
            img_id = user["profile_image_id"]
            image_data = fs.get(img_id).read()
            image = Image.open(io.BytesIO(image_data))
            st.image(image, caption="Your Profile Picture", width=200)
        else:
            st.info("No profile picture uploaded yet.")

        new_profile_image = st.file_uploader("Upload New Profile Picture", type=["jpg", "png", "jpeg"])
        if new_profile_image:
            file_id = fs.put(new_profile_image, filename=f"{user['user_name']}_profile_image")
            collection.update_one({"_id": user["_id"]}, {"$set": {"profile_image_id": file_id}})
            st.success("Profile picture updated!")
            st.rerun()



    with col2:
        st.subheader(f"{user['cat_name']}'s Profile")

        with st.form("edit_profile_form"):
            cat_weight = st.number_input("Weight (kg)", value=user.get("cat_weight", 0))
            cat_breed = st.text_input("Breed", value=user.get("cat_breed", "Unknown"))
            cat_birthdate = st.date_input("Birthdate", value=datetime.strptime(user["cat_birthdate"], "%Y-%m-%d"))
            cat_quantity = st.number_input("Daily Amount of Food (in g)", value=user.get("cat_quantity", 0))
            cat_ingredient = st.text_input("Favourite Ingredient", value=user.get("cat_ingredient", "Unknown"))
            submit_button = st.form_submit_button("Save Changes")

        if submit_button:
            collection.update_one({"_id": user["_id"]}, {
                "$set": {"cat_weight": cat_weight, "cat_breed": cat_breed,
                         "cat_birthdate": str(cat_birthdate), "cat_quantity": cat_quantity,
                         "cat_ingredient": cat_ingredient},
            })
            st.session_state.logged_in_user.update({
                "cat_weight": cat_weight,
                "cat_breed": cat_breed,
                "cat_birthdate": str(cat_birthdate),
                "cat_quantity": cat_quantity,
                "cat_ingredient": cat_ingredient,
            })
            st.success("Profile updated successfully!")
            st.rerun()

    # divider
    st.markdown("---")

    # bottom half of profile (files & notes)
    col1, col11 = st.columns([1, 1])

    # left column: upload & delete PDF/Pictures (medical records)
    with col1:
        st.subheader("Upload Medical Records")
        uploaded_files = st.file_uploader("Choose files", type=["pdf", "jpg", "png"],
                                                  accept_multiple_files=True)
        if uploaded_files:
            for uploaded_file in uploaded_files:
                file_data = uploaded_file.getvalue()
                file_id = fs.put(file_data, filename=uploaded_file.name)
                collection.update_one({"_id": user["_id"]}, {"$push": {"medical_records": file_id}})
                st.success(f"Uploaded {uploaded_file.name}")

        if st.session_state.new_upload:
            st.success("Files uploaded successfully!")
            st.session_state.new_upload = False
            st.rerun()

        # display uploaded medical records
        # #part written with help of ChatGPT
        if "medical_records" in user and isinstance(user["medical_records"], list):
            if not user["medical_records"]:
                st.warning("No medical records uploaded yet.")

            for file_id in user["medical_records"]:
                file = fs.get(file_id)
                file_name = file.filename
                file_type = file_name.split('.')[-1]

                st.write(f"📄 **{file_name}**")

                if file_type in ["jpg", "png", "jpeg"]:
                    st.image(Image.open(io.BytesIO(file.read())), caption=file_name, width=150)
                elif file_type == "pdf":
                    with fitz.open(stream=io.BytesIO(file.read()), filetype="pdf") as doc:
                        for page in doc:
                            pix = page.get_pixmap()
                            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
                            st.image(img, width=150)

                else:
                    st.warning(f"Unsupported file format: {file_type}")
                    continue


                col1, col2 = st.columns([0.2, 0.8])
                with col1:
                    if st.button(f"🗑️ Delete {file_name}", key=file_id):
                        fs.delete(file_id)
                        collection.update_one({"_id": user["_id"]}, {"$pull": {"medical_records": file_id}})
                        st.success(f"File {file_name} deleted!")
                        st.rerun()



    #right column: notepad for notes
    with col11:
        st.subheader("Notepad 📝")
        st.write("Use the Pad e.g. as a shopping list or simply to remember things!")
        note_text = st.text_area("Write something...", height=200)

        if st.button("Save Note"):
            if note_text:
                note_obj = {"_id": str(ObjectId()), "text": note_text}  # unique ID
                collection.update_one({"_id": user["_id"]}, {"$push": {"notes": note_obj}})
                st.success("Note saved!")
                st.rerun()
            else:
                st.error("Please write something to save!")

        if "notes" in user and isinstance(user["notes"], list):
            st.write("### Saved Notes:")

            for note in user["notes"]:
                if isinstance(note, dict) and "text" in note:
                    st.write(f"- {note['text']}")

    st. divider()

    if st.button("Logout"):
        st.session_state.logged_in_user = None
        st.rerun()