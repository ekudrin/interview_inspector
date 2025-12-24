import random
import pyttsx3
import streamlit as st
from questions import questions

# получить рандомный вопрос из выбранной категории
def get_random_question(category: str) -> str:
    if category not in questions.keys():
        return f"Категория {category} не найдена в словаре"
    questions_list = questions.get(category)
    return random.choice(questions_list)

# text to speech для выбранного вопроса
def play_question(question: str) -> str:
    engine = pyttsx3.init()
    engine.setProperty('voice', 'ru')
    engine.say(question)
    engine.runAndWait()


#app
st.set_page_config(page_title="Interview Inspector", page_icon="🔎")
st.title("Interview Inspector")

options = questions.keys()
selected_option = st.selectbox(
    label="Категория, из которой будет вопрос",
    options=options,
    placeholder="Выбери категорию..."
)
if st.button("Получить вопрос"):
    question = get_random_question(selected_option)
    play_question(question)
    st.text_area(label="Вопрос", value=question)



