import streamlit as st
import sqlite3

# Function to create a connection to the SQLite database
def create_connection():
    conn = sqlite3.connect('answers.db')
    return conn

# Function to create the table if it doesn't exist
def create_table(conn):
    with conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS responses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                question TEXT NOT NULL,
                answer TEXT NOT NULL
            )
        ''')

import streamlit as st

st.title("Hazel's Beauty Quiz /U+1FA77")

# Initial questions
questions = [
    "What is your name?",
    "How old are you?",
    "Are you concerned about wrinkles or fine lines?",
    "Which color would you say your complexion is?",
    "Are you looking for a glowy or matte finish on your makeup?",
    "Do you want skincare or SPF within your makeup? or Both?",
    "Do you have acne prone skin?",
    "Does makeup usually worsen your acne?",
    "Do you have acne scars?",
    "Do you have dark circles?",
    "What coverage do you like your makeup to be?",
    "What is your price range for makeup products?",
    "Do you prefer a certain applicator?",
    "Do you like your products to be cruelty free?",
    "Do you like your products to be vegan?",
    "Are there any brands you are not open to?",
    "Do you have any other concerns for makeup products?",
    ]


# Initialize session state
if 'question_index' not in st.session_state:
    st.session_state.question_index = 0

# Create database connection and table
conn = create_connection()
create_table(conn)

# Display the current question
if st.session_state.question_index < len(questions):
    question = questions[st.session_state.question_index]
    answer = st.text_input(question)

    if st.button("Submit Answer"):
        if answer:
            with conn:
                conn.execute('INSERT INTO responses (question, answer) VALUES (?, ?)', (question, answer))
            st.session_state.question_index += 1
            st.success("Answer recorded! Proceeding to the next question.")
        else:
            st.error("Please provide an answer.")

# Check if all questions have been answered
if st.session_state.question_index == len(questions):
    qskintype ="What is your skin type?"
    skin_type = st.radio(
        "What is your skin type?", ['Dry', 'Oily', 'Combination']
    )
    #picture = st.camera_input("Take a picture")
    #label = "Picture"
    with conn:
        conn.execute('INSERT INTO responses (question, answer) VALUES (?, ?)', (qskintype, skin_type))
        cursor = conn.cursor()
        cursor.execute('''SELECT * from responses''')
        result = cursor.fetchall()
        #conn.execute('INSERT INTO responses (question, answer) VALUES (?, ?)', (label, picture))
    st.success("All questions answered! Thank you!")


    st.text(result)
    st.session_state.question_index = 0  # Reset for next session
    conn.close()


    #possibly add user feed back
    #add imaging
    # i want to add feedback on products, so it can help the database on rating products best for people
  #i like the modal dialogs which includes a subscription letter
  #the balloons or raining emojis is a cool addon on top of the letter
