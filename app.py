import streamlit as st

# ------------------ Page Config ------------------
st.set_page_config(
    page_title="Love in the Line of Fire",
    layout="wide"
)

# ------------------ Hide Default UI ------------------
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

# ------------------ Menu Button (TOP LEFT, ALWAYS VISIBLE) ------------------
st.markdown("""
<style>
.menu-btn {
    position: fixed;
    top: 15px;
    left: 15px;
    z-index: 2000;   /* 🔥 HIGHER than sidebar */
}
.menu-btn button {
    font-size: 26px;
    padding: 4px 10px;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="menu-btn">', unsafe_allow_html=True)
if st.button("☰"):
    st.session_state.menu_open = not st.session_state.menu_open
st.markdown('</div>', unsafe_allow_html=True)

# ------------------ Sidebar & Content Layout ------------------
sidebar_width = "260px" if st.session_state.menu_open else "0px"
content_margin = "260px" if st.session_state.menu_open else "0px"

st.markdown(f"""
<style>
.side-menu {{
    position: fixed;
    top: 0;
    left: 0;
    height: 100%;
    width: {sidebar_width};
    background-color: #f0f2f6;
    overflow-x: hidden;
    transition: 0.3s;
    padding-top: 80px;
    z-index: 1000;   /* 👈 LOWER than menu button */
}}

.side-menu button {{
    width: 90%;
    margin: 10px;
}}

.main-content {{
    margin-left: {content_margin};
    transition: 0.3s;
    padding: 40px;
}}
</style>
""", unsafe_allow_html=True)

# ------------------ Sidebar Content ------------------
st.markdown('<div class="side-menu">', unsafe_allow_html=True)

if st.session_state.menu_open:
    if st.button("🏠 Home"):
        st.session_state.page = "Home"
    if st.button("📖 Journey of a Young Mind"):
        st.session_state.page = "Journey"
    if st.button("😊 Smiley"):
        st.session_state.page = "Smiley"

st.markdown('</div>', unsafe_allow_html=True)

# ------------------ Main Content ------------------
st.markdown('<div class="main-content">', unsafe_allow_html=True)

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

st.markdown('</div>', unsafe_allow_html=True)
