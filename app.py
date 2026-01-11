import streamlit as st

# ------------------ Page Config ------------------
st.set_page_config(
    page_title="Love in the Line of Fire",
    layout="centered"
)
st.markdown(
    """
    <style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True
)

# ------------------ Session State ------------------
if "page" not in st.session_state:
    st.session_state.page = "Home"

# ------------------ Sidebar Menu (BUTTONS) ------------------
st.sidebar.title("Menu")

if st.sidebar.button("🏠 Home"):
    st.session_state.page = "Home"

if st.sidebar.button("📖 Journey of a Young Mind"):
    st.session_state.page = "Journey"

if st.sidebar.button("😊 Smiley"):
    st.session_state.page = "Smiley"

# ------------------ Pages ------------------
if st.session_state.page == "Home":
    st.markdown(
        "<h1 style='text-align:center;'>Love in the Line of Fire</h1>",
        unsafe_allow_html=True
    )

elif st.session_state.page == "Journey":
    st.markdown("<h1>Journey of a Young Mind</h1>", unsafe_allow_html=True)
    st.write("📅 **Will be uploaded on 14th Feb, 2026**")

elif st.session_state.page == "Smiley":
    st.markdown("<h1>Smiley</h1>", unsafe_allow_html=True)
    st.write("📅 **Will be uploaded on 14th Feb, 2026**")

