import streamlit as st
import random
import time

# Initialize session state for computer choice if it doesn't exist
if 'computer_choice' not in st.session_state:
    st.session_state.computer_choice = None

# Streamlit UI
st.title("Rock, Paper, Scissors Game")
st.write("Choose an option, and I'll try to beat you!")

# User choice input
user_choice = st.selectbox("Choose rock, paper, or scissors:", ["rock", "paper", "scissors"])

# Button to confirm choice
if st.button("Confirm Choice"):
    # Introduce delay before displaying result
    with st.spinner("Thinking... 🤔"):
        time.sleep(1)  # 1 second delay

    # Generate computer choice
    st.session_state.computer_choice = random.choice(["rock", "paper", "scissors"])

    # Game logic
    if user_choice == st.session_state.computer_choice:
        result = "It's a tie!"
    elif (user_choice == "rock" and st.session_state.computer_choice == "scissors") or \
         (user_choice == "paper" and st.session_state.computer_choice == "rock") or \
         (user_choice == "scissors" and st.session_state.computer_choice == "paper"):
        result = "You win!"
    else:
        result = "You lose!"

    # Display results
    st.write(f"You chose **{user_choice}**, and the computer chose **{st.session_state.computer_choice}**.")
    st.write(result)