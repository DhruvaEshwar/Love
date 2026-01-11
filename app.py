import streamlit as st

# ------------------ Page Config ------------------
st.set_page_config(
    page_title="Love in the Line of Fire",
    layout="centered"
)

# ------------------ Hide Streamlit UI ------------------
st.markdown(
    """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .menu-box {
        border: 1px solid #ddd;
        padding: 15px;
        border-radius: 10px;
        background-color: #f9f9f9;
        margin-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ------------------ Session State ------------------
if "page" not in st.session_state:
    st.session_state.page = "Home"

if "menu_open" not in st.session_state:
    st.session_state.menu_open = False

# ------------------ Menu Toggle Button ------------------
if st.button("☰ Menu"):
    st.session_state.menu_open = not st.session_state.menu_open

# ------------------ CUSTOM MENU (NOT SIDEBAR) ------------------
if st.session_state.menu_open:
    st.markdown('<div class="menu-box">', unsafe_allow_html=True)

    if st.button("🏠 Home"):
        st.session_state.page = "Home"
        st.session_state.menu_open = False

    if st.button("📖 Journey of a Young Mind"):
        st.session_state.page = "Journey"
        st.session_state.menu_open = False

    if st.button("😊 Smiley"):
        st.session_state.page = "Smiley"
        st.session_state.menu_open = False

    st.markdown('</div>', unsafe_allow_html=True)

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
