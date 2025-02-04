import streamlit as st
from datetime import datetime, timedelta

# App title
st.title("Khogii and Handa Streak 🏆")

# Initialize session state for streak, last updated date, and daily status
if 'streak' not in st.session_state:
    st.session_state.streak = 0
if 'last_updated' not in st.session_state:
    st.session_state.last_updated = datetime.now().date()
if 'khogii_status' not in st.session_state:
    st.session_state.khogii_status = None
if 'handa_status' not in st.session_state:
    st.session_state.handa_status = None
if 'progress_saved' not in st.session_state:
    st.session_state.progress_saved = False
if 'custom_image' not in st.session_state:
    st.session_state.custom_image = None

# Healthy daily checklist
st.write("Eruul amidrahiin tuluu✅")

# Side-by-side layout for Khogii and Handa
col1, col2 = st.columns(2)

# Khogii's status (left side)
with col1:
    st.subheader("Khogii")
    khogii_option = st.radio(
        "Khogii's status:",
        ["Bi chadlaa ;))", "Hehe, za yhv2 :/"],
        key="khogii_radio"
    )

# Handa's status (right side)
with col2:
    st.subheader("Handa")
    handa_option = st.radio(
        "Handa's status:",
        ["Bi chadlaa ;))", "Hehe, za yhv2 :/"],
        key="handa_radio"
    )

# Enable the save button only if both have made selections
if khogii_option and handa_option and not st.session_state.progress_saved:
    if st.button("Save Today's Progress"):
        st.session_state.khogii_status = khogii_option
        st.session_state.handa_status = handa_option
        st.session_state.progress_saved = True

        # Streak logic (immediately after submitting)
        if st.session_state.khogii_status == "Bi chadlaa ;))" and st.session_state.handa_status == "Bi chadlaa ;))":
            # Check if the last updated date is yesterday (to ensure it's a new day)
            if st.session_state.last_updated == (datetime.now().date() - timedelta(days=1)):
                st.session_state.streak += 1
            elif st.session_state.last_updated < (datetime.now().date() - timedelta(days=1)):
                st.session_state.streak = 1  # Reset streak if more than a day has passed
            st.session_state.last_updated = datetime.now().date()
        else:
            st.session_state.streak = 0  # Reset streak if either fails

        st.success("Progress saved for today!")
else:
    st.button("Save Today's Progress", disabled=True)

# Display the streak immediately after submitting
if st.session_state.progress_saved:
    st.header(f"Current Streak: {st.session_state.streak} days 🔥")

# Upload custom image for motivation
st.subheader("Upload Your Own Motivational Image")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    st.session_state.custom_image = uploaded_file

# Display the image for motivation
if st.session_state.streak > 0:
    if st.session_state.custom_image:
        st.image(st.session_state.custom_image, caption="Keep going! You're doing great!", width=300)
    else:
        st.image("https://i.imgur.com/3JQ2qyA.png", caption="Keep going! You're doing great!", width=300)
else:
    if st.session_state.custom_image:
        st.image(st.session_state.custom_image, caption="Start fresh today!", width=300)
    else:
        st.image("https://i.imgur.com/7Q7Q7Q7.png", caption="Start fresh today!", width=300)

# Footer
st.write("Made with ❤️ by H&A")
