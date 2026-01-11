import streamlit as st

# ------------------ Page Config ------------------
st.set_page_config(
    page_title="Love in the Line of Fire",
    layout="wide"
)

# ------------------ Hide Top Right Buttons ------------------
st.markdown("""
<style>
#MainMenu {visibility: hidden;}  /* hides three dots menu */
footer {visibility: hidden;}    /* hides footer */
[data-testid="stToolbar"] {visibility: hidden !important;} /* hides fork/github buttons on Streamlit Cloud */
</style>
""", unsafe_allow_html=True)

# ------------------ Session State ------------------
if "page" not in st.session_state:
    st.session_state.page = "Home"
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# ------------------ PASSWORD ------------------
HOME_PASSWORD = "1414"

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
    st.stop()

# ------------------ LAYOUT: Fixed Left Menu ------------------
col1, col2 = st.columns([1, 4])  # 1/5th sidebar, 4/5th main content

with col1:
    # Vertical separator
    st.markdown("""
        <div style='border-right:2px solid #cccccc; height:100vh; padding-right:10px;'>
    """, unsafe_allow_html=True)
    st.markdown("## Menu")
    if st.button("🏠 Home"):
        st.session_state.page = "Home"
    if st.button("📖 Journey of a Young Mind"):
        st.session_state.page = "Journey"
    if st.button("😊 Smiley"):
        st.session_state.page = "Smiley"
    st.markdown("</div>", unsafe_allow_html=True)  # close the div

with col2:
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

