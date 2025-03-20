"""
📌 Task 6: Функция, которая проверяет, содержит ли строка все буквы алфавита
Напишите функцию is_pangram(text: str) -> bool, которая принимает строку и возвращает True, 
если в строке встречаются все буквы английского алфавита (a-z) хотя бы раз, и False в противном случае.

🔹 Пример работы:
print(is_pangram("The quick brown fox jumps over the lazy dog"))
print(is_pangram("Hello, world!"))

Ожидаемый результат:
True
False
"""

def is_pangram(text):
    # TODO: Напишите код здесь
    pass

# Тесты
assert is_pangram("The quick brown fox jumps over the lazy dog") == True
assert is_pangram("Hello, world!") == False
assert is_pangram("abcdefghijklmnopqrstuvwxyz") == True
assert is_pangram("Pack my box with five dozen liquor jugs") == True
