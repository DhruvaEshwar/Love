import streamlit as st

# ------------------ Page Config ------------------
st.set_page_config(
    page_title="Love in the Line of Fire",
    layout="wide"
)

# ------------------ Hide Streamlit Menu & Footer ------------------
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ------------------ Session State ------------------
if "page" not in st.session_state:
    st.session_state.page = "Home"

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# ------------------ Sidebar ------------------
with st.sidebar:
    st.title("Menu")

    if st.button("🏠 Home"):
        st.session_state.page = "Home"
    if st.button("📖 Journey of a Young Mind"):
        st.session_state.page = "Journey"
    if st.button("😊 Smiley"):
        st.session_state.page = "Smiley"

# ------------------ Password Protected Home Page ------------------
HOME_PASSWORD = "1234"  # 🔑 Set your password here

if st.session_state.page == "Home":
    if not st.session_state.authenticated:
        st.write("🔒 Enter Passcode to access Home page:")
        password_input = st.text_input("Passcode", type="password")
        if st.button("Enter"):
            if password_input == HOME_PASSWORD:
                st.session_state.authenticated = True
                st.success("✅ Access granted!")
                st.experimental_rerun()
            else:
                st.error("❌ Incorrect passcode")
    else:
        st.markdown(
            "<h1 style='text-align:center;'>Love in the Line of Fire</h1>",
            unsafe_allow_html=True
        )

# ------------------ Other Pages (No Password) ------------------
elif st.session_state.page == "Journey":
    st.markdown("<h1>Journey of a Young Mind</h1>", unsafe_allow_html=True)
    st.write("📅 **Will be uploaded on 14th Feb, 2026**")

elif st.session_state.page == "Smiley":
    st.markdown("<h1>Smiley</h1>", unsafe_allow_html=True)
    st.write("📅 **Will be uploaded on 14th Feb, 2026**")

