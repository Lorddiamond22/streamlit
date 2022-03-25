import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Website", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
img_contact_form = Image.open("images/yt_contact_form.png")
img_lottie_animation = Image.open("images/yt_lottie_animation.png")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hai, nama gua Diaz :wave:")
    st.title("Website Pertama Gua Dengan Python")
    st.write(
        "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Voluptatum sit maxime et."
    )
    st.write("[Download Source Code >](https://drive.google.com/file/d/1k1vNzT2dvYIpaWrblezpvM9bYRRS_sRz/view?usp=sharing)")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            Di web kali ini gua hanya ingin memberitahu kepada kalian tentang:
            - Nostrum facere sequi cum tempora, numquam veritatis quo deleniti voluptatum.
            - Nostrum facere sequi cum tempora, numquam veritatis quo deleniti voluptatum.
            - Nostrum facere sequi cum tempora, numquam veritatis quo deleniti voluptatum.
            - Nostrum facere sequi cum tempora, numquam veritatis quo deleniti voluptatum.
            

            Lorem, ipsum dolor sit amet consectetur adipisicing elit. Voluptatum sit maxime et. Voluptatum sit maxime et
            """
        )
        st.write("[My Github >](https://github.com/Lorddiamond22)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("Mengubah Background Website Dengan JavaScript")
        st.write(
            """
            Lorem, ipsum dolor sit amet consectetur adipisicing elit.
            Voluptatum sit maxime et. Nostrum facere sequi cum tempora, numquam veritatis quo deleniti voluptatum.
            Deserunt, quisquam maxime cum numquam.
            """
        )
        st.markdown("[Demo...](https://muhamaddiazzz.netlify.app)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("Website Responsive Dengan Boostrapt")
        st.write(
            """
            Lorem, ipsum dolor sit amet consectetur adipisicing elit.
            Voluptatum sit maxime et. Nostrum facere sequi cum tempora, numquam veritatis quo deleniti voluptatum.
            Deserunt, quisquam maxime cum numquam.
            """
        )
        st.markdown("[Demo...](https://muhamaddiazz.netlify.app)")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Contact Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/mdariscool@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
