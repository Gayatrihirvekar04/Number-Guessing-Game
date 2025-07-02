import streamlit as st
import random

# Set the title of the app
st.title("Number Guessing Game")

# Instructions
st.write("Welcome to the Number Guessing Game!")
st.write("You have 7 chances to guess the number. Let's start!")

# Input for lower and upper bounds
low = st.number_input("Enter Lower Bound:", value=1)
high = st.number_input("Enter Upper Bound:", value=100)

# Button to start the game
if st.button("Start Game"):
    # Generate a random number
    num = random.randint(low, high)
    attempts = 0
    max_attempts = 7

    # Store the number in session state
    st.session_state['number'] = num
    st.session_state['attempts'] = attempts
    st.session_state['max_attempts'] = max_attempts

    st.write(f"You have {max_attempts} chances to guess the number between {low} and {high}.")

# Input for user's guess
if 'number' in st.session_state:
    guess = st.number_input("Enter your guess:", value=low, min_value=low, max_value=high)

    if st.button("Submit Guess"):
        st.session_state['attempts'] += 1
        attempts = st.session_state['attempts']
        num = st.session_state['number']

        if guess == num:
            st.success(f'Correct! The number is {num}. You guessed it in {attempts} attempts.')
            # Reset the game
            del st.session_state['number']
            del st.session_state['attempts']
        elif attempts >= st.session_state['max_attempts']:
            st.error(f'Sorry! The number was {num}. Better luck next time.')
            # Reset the game
            del st.session_state['number']
            del st.session_state['attempts']
        elif guess > num:
            st.warning('Too high! Try a lower number.')
        elif guess < num:
            st.warning('Too low! Try a higher number.')
