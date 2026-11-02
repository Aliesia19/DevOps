def print_string(text):
    if not isinstance(text, str):
        print("Помилка: аргумент повинен бути рядком.")
        return

    print(text)


def check_case(text):
    if not isinstance(text, str):
        print("Помилка: аргумент повинен бути рядком.")
        return

    if not text:
        print("Рядок порожній.")
    elif not any(char.isalpha() for char in text):
        print("Рядок не містить літер.")
    elif text.isupper():
        print("Усі літери великі.")
    elif text.islower():
        print("Усі літери малі.")
    else:
        print("Регістр літер змішаний.")
