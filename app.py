import faulthandler

from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

# --- Use Local CSS ---
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

# --- Load Assets ---
lottie_asset1 = "https://lottie.host/c501012b-3e88-4fbd-9caf-b4480a704d89/qsHm55I3lw.json"
img_ib_logo = Image.open("images/IB_Logo.png")
img_cast_ut_logo = Image.open("images/CAST-UT Logo.png")

# --- Header ---
with st.container():
    st.subheader("Hi, I am Vishwa! :wave:")
    st.title("High School Student")
    st.write("I love coding and dogs")
    st.write("[Learn More >](https://thomaslulearnerportfolio.weebly.com)")

# --- Part 2 ---
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Part 2")
        st.write("##")
        st.write(
            """
            Here is a list:
            - First item
            - Second Item
            - Third Item
            """
        )
    # with right_column:
        # st_lottie(lottie_asset1, height=300, key="coding")

# --- Part 3 ---
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_ib_logo)
    with text_column:
        st.subheader("Subheader for Part 3")
        st.write(
        """
        Here is the IB logo!
        """
        )
        st.markdown("[Link to youtube!](https://youtube.com)")

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_cast_ut_logo)
    with text_column:
        st.write("Here is the CAST-UT Logo!")

## --- Contact ---
with st.container():
    st.write("---")
    st.header("Contact Me!")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/thomaslu678@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()