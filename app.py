import streamlit as st

# ------------------ Page Config ------------------
st.set_page_config(
    page_title="Love in the Line of Fire",
    layout="wide"
)

# ------------------ Hide Top Right Menu and Footer ------------------
st.markdown("""
<style>
/* Hide Streamlit menu (three dots) */
#MainMenu {visibility: hidden;}

/* Hide footer */
footer {visibility: hidden;}

/* Hide top-right Fork/GitHub buttons on Streamlit Cloud */
[data-testid="stToolbar"] {visibility: hidden !important;}
</style>
""", unsafe_allow_html=True)

# ------------------ Session State ------------------
if "page" not in st.session_state:
    st.session_state.page = "Home"

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# ------------------ PASSWORD ------------------
HOME_PASSWORD = "1234"  # 🔑 Change this to your password

# ------------------ AUTHENTICATION ------------------
if not st.session_state.authenticated:
    st.write("🔒 Enter Passcode to access the website:")
    password_input = st.text_input("Passcode", type="password", key="pwd")
    if st.button("Enter Passcode"):
        if password_input == HOME_PASSWORD:
            st.session_state.authenticated = True
            st.success("✅ Access granted!")
        else:
            st.error("❌ Incorrect passcode")
    # Stop everything else until authenticated
    st.stop()

# ------------------ MAIN WEBSITE (ONLY AFTER AUTH) ------------------

# ------------------ Sidebar (Always Open) ------------------
# Using container to mimic always-open sidebar
with st.sidebar:
    st.title("Menu")
    if st.button("🏠 Home"):
        st.session_state.page = "Home"
    if st.button("📖 Journey of a Young Mind"):
        st.session_state.page = "Journey"
    if st.button("😊 Smiley"):
        st.session_state.page = "Smiley"

# ------------------ Main Content ------------------
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
