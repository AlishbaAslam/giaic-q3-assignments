import streamlit as st
import re

def check_password_strength(password):
    score = 0
    feedback = []

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")
    
    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")
    
    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")
    
    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (e.g., !@#$%^&*).")

    return score, feedback

# Streamlit UI
st.set_page_config(page_title="Password Strength Meter", page_icon="🔐")
st.title("🔐 Password Strength Meter")
st.markdown("##### Not sure if your password is strong enough? Just type it in and let this smart app guide you! It gives you real-time feedback on how secure your password is and tips to make it even stronger.")

password = st.text_input("Enter your password", type="password")

if password:
    score, messages = check_password_strength(password)

    st.subheader("Make Your Password Stronger:")
    for msg in messages:
        st.warning(msg)

    if score == 4:
        st.success("✅ Strong Password!")
    elif score == 3:
        st.info("⚠️ Moderate Password - Consider adding more security features.")
    else:
        st.error("❌ Weak Password - Improve it using the suggestions above.")
