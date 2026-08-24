import streamlit as st
import random

st.markdown("""
<style>

.stApp {
    background-color: #121212;
    color: white;
}

.stButton > button {
    background-color: #FF5722;
    color: white;
    border-radius: 12px;
    border: none;
    font-size: 18px;
    font-weight: bold;
}

.stButton > button:hover {
    background-color: #E64A19;
}

</style>
""", unsafe_allow_html=True)

st.title("🎯 Number Guessing Game")

st.write("Guess a number between 1 and 100!")


if "jack" not in st.session_state:
    st.session_state.jack = random.randint(1, 100)

if "count" not in st.session_state:
    st.session_state.count = 0

if "game_over" not in st.session_state:
    st.session_state.game_over = False


guess = st.number_input(
    "Enter your guess:",
    min_value=1,
    max_value=100,
    step=1
)


if st.button("Check Guess"):

    if st.session_state.game_over:

        st.warning("Game is already over. Start a new game!")

    else:

        st.session_state.count += 1

        if guess < st.session_state.jack:
            st.info("📈 Choose a greater number!")

        elif guess > st.session_state.jack:
            st.info("📉 Choose a lower number!")

        else:
            st.success("🎉 Congratulations! You won!")

            st.write(
                "Attempts:",
                st.session_state.count
            )

            st.session_state.game_over = True


st.write(f"🔢 Attempts: {st.session_state.count}")


if st.button("🔄 New Game"):

    st.session_state.jack = random.randint(1, 100)
    st.session_state.count = 0
    st.session_state.game_over = False

    st.rerun()