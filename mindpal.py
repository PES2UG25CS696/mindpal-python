import streamlit as st
import os
from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.title("🧠 MindPal – AI Learning Assistant")
st.write("Ask any question and choose your explanation level!")

level = st.selectbox(
    "Choose explanation level:",
    ["5th Grade", "8th Grade", "High School", "University"]
)

question = st.text_input("Type your question:")

if st.button("Explain"):
    if question.strip() == "":
        st.error("Please enter a question!")
    else:
        prompt = (
            f"Explain the following question for a {level} level:\n"
            f"Question: {question}"
        )

        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": "You are MindPal, a friendly educational tutor."},
                {"role": "user", "content": prompt}
            ]
        )

        answer = response.choices[0].message.content
        st.success(answer)