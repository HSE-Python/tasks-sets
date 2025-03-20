"""
📌 Task 5: Функция для удаления запрещённых слов из текста
Напишите функцию censor_text(text: str, banned_words: set) -> str, которая принимает текст и 
множество запрещённых слов, возвращает текст без этих слов.

🔹 Пример работы:
print(censor_text("Python — лучший язык программирования", {"лучший", "язык"}))

Ожидаемый результат:
Python — программирования

💡 Подсказка: Разбейте текст .split().
Удалите слова, которые есть в banned_words.
Соберите обратно .join().
"""

def censor_text(text, banned_words):
    # TODO: Напишите код здесь
    pass

# Тесты
assert censor_text("Python — лучший язык программирования", {"лучший", "язык"}) == "Python — программирования"
assert censor_text("Hello world", {"world"}) == "Hello"
assert censor_text("Spam and eggs", {"Spam"}) == "and eggs"
assert censor_text("Nothing to censor", {"something"}) == "Nothing to censor"
