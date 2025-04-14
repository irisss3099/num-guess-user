import streamlit as st
import random

# Set page config
st.set_page_config(page_title="Guess the Number (Two Player)", page_icon="🎯", layout="centered")

# Background color
st.markdown("""
    <style>
        body {
            background-color: #e6f7ff;
        }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
    <h1 style='text-align: center; color: #007acc;'>🎯 Two Player Guess the Number</h1>
    <p style='text-align: center; font-size: 18px;'>Player 1 sets a number. Player 2 tries to guess it!</p>
""", unsafe_allow_html=True)

# Initialize game state
if 'target_number' not in st.session_state:
    st.session_state.target_number = None
if 'attempts' not in st.session_state:
    st.session_state.attempts = 0
if 'game_over' not in st.session_state:
    st.session_state.game_over = False

# Game logic
if st.session_state.target_number is None:
    with st.form("set_number_form"):
        number = st.number_input("Player 1: Enter a number between 1 and 100 (Player 2, look away!)", min_value=1, max_value=100, step=1)
        submitted = st.form_submit_button("Set Number")
        if submitted:
            st.session_state.target_number = int(number)
            st.success("Number set! Player 2, start guessing.")

elif not st.session_state.game_over:
    with st.form("guess_form"):
        guess = st.number_input("Player 2: Guess the number", min_value=1, max_value=100, step=1)
        guess_btn = st.form_submit_button("Guess")

        if guess_btn:
            st.session_state.attempts += 1
            if guess < st.session_state.target_number:
                st.info("Too low! Try a higher number.")
            elif guess > st.session_state.target_number:
                st.info("Too high! Try a lower number.")
            else:
                st.session_state.game_over = True

if st.session_state.game_over:
    st.success(f"🎉 Correct! You guessed the number {st.session_state.target_number} in {st.session_state.attempts} attempts!")
    if st.button("Play Again"):
        for key in ['target_number', 'attempts', 'game_over']:
            del st.session_state[key]
        st.rerun()

# Footer
st.markdown("""
<hr style='border: 1px solid #b3d9ff;'>
<p style='text-align: center; font-size: 14px;'>Developed by Sabila Aleem ❤</p>
""", unsafe_allow_html=True)


 


