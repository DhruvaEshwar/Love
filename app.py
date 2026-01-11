import streamlit as st

# ------------------ Page Config ------------------
st.set_page_config(
    page_title="Love in the Line of Fire",
    layout="centered"
)

# ------------------ Custom CSS ------------------
st.markdown(
    """
    <style>
    /* Hide Streamlit UI */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Menu button - absolute top-left */
    .menu-btn {
        position: fixed;
        top: 8px;
        left: 8px;
        z-index: 2001;
    }

    /* Side menu */
    .side-menu {
        position: fixed;
        top: 0;
        left: 0;
        height: 100%;
        width: 260px;
        background-color: #f9f9f9;
        padding: 20px;
        box-shadow: 2px 0 10px rgba(0,0,0,0.15);
        z-index: 2000;
    }

    /* Push content right when menu is open */
    .content-shift {
        margin-left: 260px;
        transition: margin-left 0.2s ease;
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

# ------------------ Menu Button ------------------
st.markdown('<div class="menu-btn">', unsafe_allow_html=True)
if st.button("☰"):
    st.session_state.menu_open = not st.session_state.menu_open
st.markdown('</div>', unsafe_allow_html=True)

# ------------------ Side Menu ------------------
if st.session_state.menu_open:
    st.markdown('<div class="side-menu">', unsafe_allow_html=True)
    st.markdown("### Menu")

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

# ------------------ Content Wrapper ------------------
content_class = "content-shift" if st.session_state.menu_open else ""

st.markdown(f'<div class="{content_class}">', unsafe_allow_html=True)

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

st.markdown('</div>', unsafe_allow_html=True)
