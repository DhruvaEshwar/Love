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

    /* Menu button */
    .menu-btn {
        position: fixed;
        top: 8px;
        left: 8px;
        z-index: 3000;
    }

    /* Side menu */
    .side-menu {
        position: fixed;
        top: 0;
        left: 0;
        width: 260px;
        height: 100vh;
        background-color: #f9f9f9;
        padding: 20px;
        box-shadow: 2px 0 12px rgba(0,0,0,0.2);
        z-index: 2000;
    }

    /* Shift ENTIRE app right */
    .shift-right {
        transform: translateX(260px);
        transition: transform 0.25s ease;
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

# ------------------ Inject shift class ------------------
if st.session_state.menu_open:
    st.markdown(
        """
        <script>
        const app = window.parent.document.querySelector('section.main');
        if (app) { app.classList.add('shift-right'); }
        </script>
        """,
        unsafe_allow_html=True
    )
else:
    st.markdown(
        """
        <script>
        const app = window.parent.document.querySelector('section.main');
        if (app) { app.classList.remove('shift-right'); }
        </script>
        """,
        unsafe_allow_html=True
    )

# ------------------ Side Menu ------------------
if st.session_state.menu_open:
    st.markdown('<div class="side-menu">', unsafe_allow_html=Tr

