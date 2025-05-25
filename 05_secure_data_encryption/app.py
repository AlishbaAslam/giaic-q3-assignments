import streamlit as st
import hashlib
from cryptography.fernet import Fernet

# Generate and initialize Fernet cipher (Use secure key storage in production)
KEY = Fernet.generate_key()
cipher = Fernet(KEY)

# Session state for data and attempts
if "stored_data" not in st.session_state:
    st.session_state.stored_data = {}

if "failed_attempts" not in st.session_state:
    st.session_state.failed_attempts = 0

if "authorized" not in st.session_state:
    st.session_state.authorized = True  # Initially authorized

# Helper: Hash passkey
def hash_passkey(passkey):
    return hashlib.sha256(passkey.encode()).hexdigest()

# Helper: Encrypt text
def encrypt_data(text):
    return cipher.encrypt(text.encode()).decode()

# Helper: Decrypt text
def decrypt_data(encrypted_text, passkey):
    hashed = hash_passkey(passkey)
    for key, value in st.session_state.stored_data.items():
        if key == encrypted_text and value["passkey"] == hashed:
            st.session_state.failed_attempts = 0
            return cipher.decrypt(encrypted_text.encode()).decode()
    st.session_state.failed_attempts += 1
    return None

# UI: Title and Sidebar
st.set_page_config(page_title="Secure Data App", page_icon="🛡️")
st.title("🛡️ Secure Data Encryption System")

menu = ["Home", "Store Data", "Retrieve Data", "Login"]
choice = st.sidebar.selectbox("Navigation", menu)

# Page: Home
if choice == "Home":
    st.subheader("🏠 Welcome")
    st.write("Use this app to **securely store and retrieve data** using encryption and hashed passkeys.")

# Page: Store Data
elif choice == "Store Data":
    st.subheader("📂 Store Data Securely")
    user_data = st.text_area("Enter Data:")
    passkey = st.text_input("Enter Passkey:", type="password")

    if st.button("Encrypt & Save"):
        if user_data and passkey:
            encrypted = encrypt_data(user_data)
            hashed = hash_passkey(passkey)
            st.session_state.stored_data[encrypted] = {"encrypted_text": encrypted, "passkey": hashed}
            st.success("✅ Data stored securely!")
            st.code(encrypted, language="text")
        else:
            st.error("⚠️ Please provide both data and a passkey.")

# Page: Retrieve Data
elif choice == "Retrieve Data":
    if not st.session_state.authorized:
        st.warning("🔒 You must reauthorize first.")
        st.stop()

    st.subheader("🔍 Retrieve Your Data")
    encrypted_text = st.text_area("Enter Encrypted Data:")
    passkey = st.text_input("Enter Passkey:", type="password")

    if st.button("Decrypt"):
        if encrypted_text and passkey:
            result = decrypt_data(encrypted_text, passkey)
            if result:
                st.success(f"✅ Decrypted Data: {result}")
            else:
                attempts_left = 3 - st.session_state.failed_attempts
                st.error(f"❌ Incorrect passkey! Attempts left: {attempts_left}")
                if st.session_state.failed_attempts >= 3:
                    st.warning("🚫 Too many failed attempts! Redirecting to Login...")
                    st.session_state.authorized = False
                    st.experimental_rerun()
        else:
            st.error("⚠️ Both fields are required!")

# Page: Login
elif choice == "Login":
    st.subheader("🔑 Reauthorization")
    master_pass = st.text_input("Enter Master Password:", type="password")

    if st.button("Login"):
        if master_pass == "admin123":  # Demo password
            st.session_state.failed_attempts = 0
            st.session_state.authorized = True
            st.success("✅ Reauthorized successfully! Go to 'Retrieve Data'.")
        else:
            st.error("❌ Incorrect master password.")