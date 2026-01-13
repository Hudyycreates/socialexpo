import streamlit as st
import random

questions = [
        "What's the most 'Warsaw' thing you've seen today?",
        "On a scale of 1-10, how much are you procrastinating right now?",
        "If you could replace one professor with a celebrity, who's it going to be?",
        "What’s your secret survival tip for the winter weather here?",
        "I'm on a mission to meet 5 new people—are you usually a 'social' or 'leave me alone' type?",
        "If you won 1000 PLN right now, what's the first thing you're buying?",
        "What's the best hidden spot on campus that nobody knows about?",
        "What’s one small thing that can instantly make your day better?",
        "If you could have any job for just one day, what would it be?",
        "If you could visit one place in the world, where would it be?",
        "What’s one thing you like that you think I should try?",
        "What’s the best compliment you’ve ever received?",
        "How do you think your friends would describe you?",
        "If you were a different gender for a day, what’s the first thing you’d do?",
        "What is something you’re obsessed with right now?",
        "What’s one thing about uni that always makes you laugh?",
        "What are you studying right now? Is that what you see yourself doing, or do you have another passion?"
    ]


# --- ADDED LINE 1: This checks if we already have a question saved ---
if "saved_question" not in st.session_state:
   st.session_state.saved_question = "Press the button to start"

# --- NEW: Initialize the counter memory ---
if "people_count" not in st.session_state:
    st.session_state.people_count = 0

st.title("🚀 --- THE 5-PEOPLE CHALLENGE --- 🚀")

# --- NEW: Show progress to the person you're talking to ---
st.subheader(f"Progress: {st.session_state.people_count} / 5 People Met")
st.progress(st.session_state.people_count / 5)

st.write("Find someone, take a breath, and press ENTER to get your question.")
st.button("READY?") 

# --- ADDED LINE 2: This button updates the saved question ---
if st.button("Click for Random Question"):
    st.session_state.saved_question = random.choice(questions)

# --- MODIFIED: Use the saved question from session_state ---
st.info(f"YOUR MISSION:👉 {st.session_state.saved_question} ")

st.write("\n--- Talk to them! ---")

# --- UPDATED: This button now actually counts the people! ---
if st.button("MISSION ACCOMPLISHED ✅"):
    if st.session_state.people_count < 5:
        st.session_state.people_count += 1
    st.balloons()

#This is where they can rate my conversation
st.write("[HAND PHONE TO THEM]")
rating = st.text_input("How was the vibe? Rate from 1-10 or an Emoji: ")

if rating:
  st.write(f"Nice! Logged a '{rating}' vibe. Thats one person closer to your goal")
  st.write("Go get the next one! ")

#When moving from terminal to web tool ie stremlit, we need to chane 'print' to st.text and 'input' to st.button so they
#...can be more suitable for the website
