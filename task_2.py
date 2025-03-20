"""
📌 Task 2: Функция для проверки анаграмм
Напишите функцию is_anagram(word1: str, word2: str) -> bool, которая принимает два слова и 
возвращает True, если они являются анаграммами, и False в противном случае.

🔹 Пример работы:
print(is_anagram("listen", "silent"))
print(is_anagram("hello", "world"))

Ожидаемый результат:
True
False
"""

def is_anagram(word1, word2):
    # TODO: Напишите код здесь
    pass

# Тесты
assert is_anagram("listen", "silent") == True
assert is_anagram("hello", "world") == False
assert is_anagram("evil", "vile") == True
assert is_anagram("python", "typhon") == True
assert is_anagram("test", "taste") == False
