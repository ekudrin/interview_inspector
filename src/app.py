import random
import pyttsx3
from questions import questions


def get_random_question(category: str) -> str:
    if category not in questions.keys():
        return f"Категория {category} не найдена в словаре"
    questions_list = questions.get(category)
    return random.choice(questions_list)

def play_question(question: str) -> str:
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(question)
    engine.runAndWait()


if __name__ == "__main__":
    while True:
        print("Выбери категорию вопроса: ")
        category = input("Статистика \n SQL \n Python \n Data Science \n Machine Learning \n (Exit для выхода) \n")
        if category == "Exit":
            break
        question  = get_random_question(category)
        print(question)
        play_question(question)
        input("(Enter для вывода следующего вопроса) \n")
