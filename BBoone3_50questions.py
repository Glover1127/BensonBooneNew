import streamlit as st
import random
import pandas as pd

# Trivia data structure (unchanged)
questions = [{"question": "Which show did Benson Boone audition for?", "options": ["America's Got Talent", "American Idol", "The Voice",
    {"question": "What genre of music is Benson Boone best known for?", "options": ["Pop", "Jazz", "Country"], "answer": "Pop", "difficulty": "Easy"},
    {"question": "What social media platform does Benson Boone use most frequently?", "options": ["Instagram", "TikTok", "Twitter"], "answer": "TikTok", "difficulty": "Easy"},
    {"question": "Which hit song did Benson Boone release in 2024?", "options": ["In the Stars", "Beautiful Things", "Before You"], "answer": "Beautiful Things", "difficulty": "Medium"},
    {"question": "Benson Boone was a contestant on which season of American Idol?", "options": ["19", "18", "20"], "answer": "19", "difficulty": "Hard"},
    {"question": "Who mentored Benson Boone early in his music career?", "options": ["Simon Cowell", "Dan Reynolds", "Adam Levine"], "answer": "Dan Reynolds", "difficulty": "Hard"},
    {"question": "What musical instrument did Benson Boone teach himself during high school?", "options": ["Guitar", "Drums", "Piano"], "answer": "Piano", "difficulty": "Medium"},
    {"question": "What year did Benson Boone gain major attention on TikTok?", "options": ["2020", "2019", "2021"], "answer": "2020", "difficulty": "Medium"},
    {"question": "Which country has Benson Boone toured in outside the US?", "options": ["Canada", "Australia", "United Kingdom"], "answer": "United Kingdom", "difficulty": "Hard"},
    {"question": "Which streaming platform helped propel Boone"s career?", "options": ["Spotify", "Apple Music", "SoundCloud"], "answer": "Spotify", "difficulty": "Easy"},
    {"question": "What’s the theme of Benson Boone’s song "In the Stars"?", "options": ["Love", "Grief", "Friendship"], "answer": "Grief", "difficulty": "Medium"},
    {"question": "Which city did Benson Boone grow up in?", "options": ["Seattle", "Monroe", "Spokane"], "answer": "Monroe", "difficulty": "Hard"},
    {"question": "What is Benson Boone"s vocal range known for?", "options": ["Bass", "Falsetto", "Tenor"], "answer": "Falsetto", "difficulty": "Medium"},
    {"question": "How did Boone respond after withdrawing from American Idol?", "options": ["Started a podcast", "Released original music", "Became a producer"], "answer": "Released original music", "difficulty": "Easy"},
    {"question": "Benson Boone signed with which artist’s record label?", "options": ["Post Malone", "Dan Reynolds", "Charlie Puth"], "answer": "Dan Reynolds", "difficulty": "Hard"},
    {"question": "What does Boone often say inspires his lyrics?", "options": ["Books", "Life experiences", "Movies"], "answer": "Life experiences", "difficulty": "Medium"},
    {"question": "What platform did Benson Boone use to tease unreleased music?", "options": ["YouTube Shorts", "TikTok", "Twitch"], "answer": "TikTok", "difficulty": "Easy"},
    {"question": "What instrument is featured in most of Boone’s ballads?", "options": ["Guitar", "Piano", "Violin"], "answer": "Piano", "difficulty": "Medium"},
    {"question": "Which of these is NOT a Benson Boone song?", "options": ["Ghost Town", "Before You", "Sunflower"], "answer": "Sunflower", "difficulty": "Easy"},
    {"question": "Which hairstyle is Benson Boone most known for?", "options": ["Buzz cut", "Curly shag", "Pompadour"], "answer": "Pompadour", "difficulty": "Medium"},
    {"question": "How old was Benson Boone when he went viral?", "options": ["17", "18", "19"], "answer": "18", "difficulty": "Hard"},
    {"question": "What is the central emotion in "Ghost Town"?", "options": ["Anger", "Loneliness", "Excitement"], "answer": "Loneliness", "difficulty": "Medium"},
    {"question": "What year did Benson Boone release "Ghost Town"?", "options": ["2020", "2021", "2022"], "answer": "2021", "difficulty": "Easy"},
    {"question": "What is the name of Benson Boone’s 2023 tour?", "options": ["Echoes Tour", "Fireworks and Rollerblades Tour", "Starboy Tour"], "answer": "Fireworks and Rollerblades Tour", "difficulty": "Hard"},
    {"question": "What genre blend best describes Boone’s sound?", "options": ["Pop-Rock", "Jazz-Fusion", "Hip-Hop"], "answer": "Pop-Rock", "difficulty": "Medium"},
    {"question": "What personal experience does Boone cite for "Before You"?", "options": ["Breakup", "New relationship", "Loss of a friend"], "answer": "New relationship", "difficulty": "Medium"},
    {"question": "Which TV show invited Benson Boone as a guest after "Ghost Town"?", "options": ["Ellen", "Jimmy Fallon", "Saturday Night Live"], "answer": "Jimmy Fallon", "difficulty": "Hard"},
    {"question": "Which platform helped "Beautiful Things" trend?", "options": ["Instagram", "YouTube", "TikTok"], "answer": "TikTok", "difficulty": "Easy"},
    {"question": "What does Boone often wear on stage?", "options": ["Leather jackets", "Oversized hoodies", "Suits"], "answer": "Oversized hoodies", "difficulty": "Medium"},
    {"question": "Which element is often in Boone’s music videos?", "options": ["Nature", "Neon lights", "Cityscapes"], "answer": "Nature", "difficulty": "Medium"},
    {"question": "What state does Boone currently reside in?", "options": ["California", "Utah", "Washington"], "answer": "California", "difficulty": "Hard"},
    {"question": "What makes Benson Boone’s live shows unique?", "options": ["He plays multiple instruments", "He dances", "He paints live"], "answer": "He plays multiple instruments", "difficulty": "Medium"},
    {"question": "Benson Boone released music under which distribution company?", "options": ["AWAL", "DistroKid", "TuneCore"], "answer": "AWAL", "difficulty": "Hard"},
    {"question": "How tall is Benson Boone?", "options": ["5"10", "6"1", "6"3"], "answer": "6"1", "difficulty": "Medium"},
    {"question": "What high school did Boone attend?", "options": ["Sky Valley High", "Monroe High School", "Cascade High"], "answer": "Monroe High School", "difficulty": "Hard"},
    {"question": "What does Boone often do before performing?", "options": ["Meditate", "Drink tea", "Jump rope"], "answer": "Drink tea", "difficulty": "Medium"},
    {"question": "Who directed the "Ghost Town" music video?", "options": ["Jake Schreier", "Andrew Donoho", "None – self-directed"], "answer": "None – self-directed", "difficulty": "Hard"},
    {"question": "How many siblings does Benson Boone have?", "options": ["Two", "Four", "Five"], "answer": "Four", "difficulty": "Hard"},
    {"question": "What’s Benson Boone’s middle name?", "options": ["James", "Taylor", "Ray"], "answer": "Ray", "difficulty": "Hard"},
    {"question": "Where did Benson Boone shoot the "Beautiful Things" video?", "options": ["Utah", "Montana", "Canada"], "answer": "Montana", "difficulty": "Hard"},
    {"question": "What year did Boone leave American Idol?", "options": ["2020", "2021", "2022"], "answer": "2021", "difficulty": "Easy"},
    {"question": "What fan nickname is sometimes used for Boone?", "options": ["Booneys", "Ghosties", "Boone Squad"], "answer": "Ghosties", "difficulty": "Hard"},
    {"question": "Which color is often used in Benson Boone’s album covers?", "options": ["Blue", "Black", "White"], "answer": "Blue", "difficulty": "Medium"},
    {"question": "What sport did Benson Boone do in high school?", "options": ["Diving", "Soccer", "Track"], "answer": "Diving", "difficulty": "Medium"}
], "answer": "American Idol", "difficulty": "Easy"},
    {"question": "Which platform made Benson Boone famous first?", "options": ["YouTube", "Instagram", "TikTok"], "answer": "TikTok", "difficulty": "Easy"},
    {"question": "What was Benson Boone's first major hit song?", "options": ["Sugar Sweet", "Ghost Town", "Beautiful Things"], "answer": "Ghost Town", "difficulty": "Easy"},
    {"question": "Benson Boone primarily plays what instrument?", "options": ["Violin", "Piano", "Drums"], "answer": "Piano", "difficulty": "Medium"},
    {"question": "In what month was Benson Boone born?", "options": ["June", "October", "December"], "answer": "June", "difficulty": "Medium"},
    {"question": "Which U.S. state is Benson Boone originally from?", "options": ["California", "Washington", "Texas"], "answer": "Washington", "difficulty": "Medium"},
    {"question": "Which major record label signed Benson Boone first?", "options": ["Warner Records", "Sony Music", "Capitol Records"], "answer": "Warner Records", "difficulty": "Hard"}
]

# Shuffle questions once
if 'shuffled_questions' not in st.session_state:
    st.session_state.shuffled_questions = random.sample(questions, len(questions))
    st.session_state.current_q = 0
    st.session_state.answers = {}
    st.session_state.score = 0
    st.session_state.next_q = False

# Initialize leaderboard
if 'leaderboard' not in st.session_state:
    st.session_state.leaderboard = pd.DataFrame(columns=['Name', 'Score'])

st.title("🎤 Benson Boone Trivia Game 🎶")

user_name = st.text_input("Enter your name to start:")

if user_name:
    q_index = st.session_state.current_q
    if q_index < len(st.session_state.shuffled_questions):
        q = st.session_state.shuffled_questions[q_index]
        st.subheader(f"Question {q_index+1}: ({q['difficulty']})")
        selected = st.radio(q['question'], q['options'], key=f"question_{q_index}")

        if st.button("Next Question"):
            st.session_state.answers[q_index] = selected
            if selected == q['answer']:
                st.session_state.score += 1
            st.session_state.next_q = True

        if st.session_state.next_q:
            st.session_state.current_q += 1
            st.session_state.next_q = False
            st.rerun()  # Changed from st.experimental_rerun()

    else:
        st.success(f"{user_name}, your final score is {st.session_state.score}/{len(st.session_state.shuffled_questions)}")
        new_entry = pd.DataFrame([[user_name, st.session_state.score]], columns=['Name', 'Score'])
        st.session_state.leaderboard = pd.concat([st.session_state.leaderboard, new_entry], ignore_index=True)
        st.session_state.leaderboard = st.session_state.leaderboard.sort_values(by='Score', ascending=False)

        if st.button("Play Again"):
            for key in ['shuffled_questions', 'current_q', 'answers', 'score', 'next_q']:
                if key in st.session_state:
                    del st.session_state[key]
            st.rerun()  # Changed from st.experimental_rerun()

    st.header("🏆 Leaderboard")
    st.dataframe(st.session_state.leaderboard.reset_index(drop=True))