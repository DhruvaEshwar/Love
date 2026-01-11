import streamlit as st

# ------------------ Page Config ------------------
st.set_page_config(
    page_title="Love in the Line of Fire",
    layout="wide"
)

# ------------------ Hide Default Streamlit UI ------------------
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
header {visibility: hidden;}
footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ------------------ Session State ------------------
if "page" not in st.session_state:
    st.session_state.page = "Home"

if "menu_open" not in st.session_state:
    st.session_state.menu_open = False

# ------------------ TOP-LEFT MENU BUTTON ------------------
col1, col2 = st.columns([1, 20])

with col1:
    if st.button("☰"):
        st.session_state.menu_open = not st.session_state.menu_open

# ------------------ SIDEBAR (REAL STREAMLIT SIDEBAR) ------------------
if st.session_state.menu_open:
    with st.sidebar:
        st.title("Menu")

        if st.button("🏠 Home"):
            st.session_state.page = "Home"

        if st.button("📖 Journey of a Young Mind"):
            st.session_state.page = "Journey"

        if st.button("😊 Smiley"):
            st.session_state.page = "Smiley"

# ------------------ MAIN CONTENT ------------------
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

