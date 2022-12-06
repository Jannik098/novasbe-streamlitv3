# # ** DALL E PROMPT GENERATOR**

#Importing openai module and keeping API key secret with streamlit backend
import os
import openai
import streamlit as st
openai.api_key = st.secrets["API_KEY"]

# # Streamlit Web App

#Page configurations
st.set_page_config(page_title="Nova SBE - DALL E Team", page_icon=":tada:", layout="wide")


#Use streamlits built in session state to "save" things. This is helpful for pagination and saving things while creating new streamlit sessions
if "page" not in st.session_state:
    st.session_state["page"] = 1

if "theme" not in st.session_state:
    st.session_state["theme"] = "You are missing a theme. Please go to back to Page 1"

if "subject" not in st.session_state:
    st.session_state["subject"] = "You are missing a subject. Please go to back to Page 2"

if "action" not in st.session_state:
    st.session_state["action"] = "You are missing an action. Please go to back to Page 3"

if "landscape" not in st.session_state:
    st.session_state["landscape"] = "You are missing a landscape. Please go to back to Page 4"


# Add a title and intro text
st.title('DALL-E 2 WEB APP')
st.subheader('This is a web app to allow Nova students to easily play around with AI image generation!')
st.text('Simply answer our questions and we will help you to create your first AI image')
st.text('Please select something in the selectbox and then navigate this web app with the Next&Previous buttons')
st.text('Have Fun!!')


#To show which page we are at right now
pagination = st.empty()

#buttons to interact with web app and continue to new pages or in other words create new sessions
next_button = st.button("Next")
if next_button:
    if st.session_state["page"] < 5:
        st.session_state["page"] += 1
        with pagination.container():
            st.write("Page")
            st.write(st.session_state.page)
    else:
        pagination.write("You've came to the last page already")

previous_button = st.button("Previous")
if previous_button:
    if st.session_state["page"] > 1:
        st.session_state["page"] -= 1
        with pagination.container():
            st.write("Page")
            st.write(st.session_state.page)
    else:
        pagination.write("There is no previous page")


#The following code pulls up the questions and input boxes on the correct page and saves the input in the session state variables defined earlier

if st.session_state["page"] == 1:
    theme_list = ['Select Theme', "Oil painting", "Picasso Painting", "Watercolor", "Pixel Art", "Digital Art", "Dramatic Lighting", "Unreal Engine", "Photorealistic"]
    theme_result = st.selectbox("Select your image theme:", theme_list)
    st.write(f'You have picked {theme_result}')
    st.session_state.theme = theme_result


if st.session_state["page"] == 2:
    subject_list = ['Select Subject', "Panda", "Cat", "Avocado", "Robots", "Astronaut", "Superhero", "Villain"]
    subject_result = st.selectbox("Select your image subject:", subject_list)
    st.write(f'You have picked {subject_result}')
    st.session_state.subject = subject_result

if st.session_state["page"] == 3:
    action_list = ['Select Action', "Eating", "Sleeping", "Fighting", "Running", "Surfing", "Painting", "Sneezing", "Exploring", "Skateboarding"]
    action_result = st.selectbox("Select what your subject is doing:", action_list)
    st.write(f'You have picked {action_result}')
    st.session_state.action = action_result

if st.session_state["page"] == 4:
    landscape_list = ['Select Landscape', "Field", "Highway", "Tokyo Crossing", "Lake", "Sunset Scenery", "Mountains", "Futuristic City Scene"]
    landscape_result = st.selectbox("Select what landscape you are in:", landscape_list)
    st.write(f'You have picked {landscape_result}')
    st.session_state.landscape = landscape_result

if st.session_state["page"] == 5:
    st.write("This is the last page and where the magic happens. This is your final prompt:")
    st.write(f'{st.session_state.theme} of a {st.session_state.subject} {st.session_state.action} on {st.session_state.landscape}')
    prompt_text = str(f'{st.session_state.theme} of a {st.session_state.subject} {st.session_state.action} on {st.session_state.landscape}')
    #This will create the image according to the users input
    response = openai.Image.create(
        prompt = prompt_text, 
        n = 2, 
        size = '512x512'
    )
    image_url = response['data'][0]['url']
    st.write("Please click the link below to view your AI-generated image!!!")
    st.write(image_url)
