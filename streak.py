import streamlit as st
from datetime import datetime, timedelta

# App title - Centered
st.markdown("<h1 style='text-align: center;'>Khogii and Handa Streak 🏆</h1>", unsafe_allow_html=True)

# Initialize session state
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
if 'show_image' not in st.session_state:
    st.session_state.show_image = False  # Track whether to show image

# Centered healthy habit text
st.markdown("<h3 style='text-align: center;'>Eruul amidrahiin tuluu ✅</h3>", unsafe_allow_html=True)

# Two columns layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("Khogii")
    khogii_option = st.radio(
        "Khogii's status:",
        ["Bi chadlaa ;))", "Hehe, za yhv2 :/"],
        key="khogii_radio"
    )

with col2:
    st.subheader("Handa")
    handa_option = st.radio(
        "Handa's status:",
        ["Bi chadlaa ;))", "Hehe, za yhv2 :/"],
        key="handa_radio"
    )

# Centered Save button
st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
if khogii_option and handa_option and not st.session_state.progress_saved:
    if st.button("Save Today's Progress"):
        st.session_state.khogii_status = khogii_option
        st.session_state.handa_status = handa_option
        st.session_state.progress_saved = True
        st.session_state.show_image = True  # Enable image display
        
        # Streak logic
        if st.session_state.khogii_status == "Bi chadlaa ;))" and st.session_state.handa_status == "Bi chadlaa ;))":
            if st.session_state.last_updated == (datetime.now().date() - timedelta(days=1)):
                st.session_state.streak += 1
            elif st.session_state.last_updated < (datetime.now().date() - timedelta(days=1)):
                st.session_state.streak = 1
            else:
                st.session_state.streak = 1
            st.session_state.last_updated = datetime.now().date()
        else:
            st.session_state.streak = 0
        
        # 🎈 Trigger balloon animation!
        st.balloons()
        
        st.success("Progress saved for today!")
else:
    st.button("Save Today's Progress", disabled=True)
st.markdown("</div>", unsafe_allow_html=True)

# Centered streak count
st.markdown(f"<h2 style='text-align: center;'>Current Streak: {st.session_state.streak} days 🔥</h2>", unsafe_allow_html=True)

# Display image only if progress has been saved
if st.session_state.show_image:
    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
    st.image("us.jpg", caption="Keep going! You're doing great!", width=500)  # Increased size
    st.markdown("</div>", unsafe_allow_html=True)

# Centered footer
st.markdown("<p style='text-align: center;'>Made with ❤️ by H&A</p>", unsafe_allow_html=True)
