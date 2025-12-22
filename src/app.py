import random

from questions import questions


def get_random_question(category: str) -> str:
    if category not in questions.keys():
        return f"Категория {category} не найдена в словаре"
    questions_list = questions.get(category)
    return random.choice(questions_list)


if __name__ == "__main__":
    while True:
        print("Выбери категорию вопроса: ")
        category = input("Статистика \n SQL \n Python \n Data Science \n Machine Learning \n (Exit для выхода) \n")
        if category == "Exit":
            break
        print(get_random_question(category))
        input("(Enter для вывода следующего вопроса) \n")
