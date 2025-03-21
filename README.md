# Практические задачи по множествам (set)

## Task 1
Функция для нахождения уникальных элементов двух списков  
Напишите функцию `unique_elements(lst1, lst2)`, которая принимает два списка `lst1` и `lst2` 
и возвращает множество элементов, которые есть только в одном из списков (симметрическая разность).

🔹 Пример работы:

```python
print(unique_elements([1, 2, 3, 4], [3, 4, 5, 6]))
```

Ожидаемый результат:

```python
{1, 2, 5, 6}
```

## Task 2
Функция для проверки анаграмм  
Напишите функцию `is_anagram(word1, word2)`, которая принимает два слова и 
возвращает `True`, если они являются анаграммами, и `False` в противном случае.

🔹 Пример работы:

```python
print(is_anagram("listen", "silent"))
print(is_anagram("hello", "world"))
```

Ожидаемый результат:

```python
True
False
```

## Task 3
Функция для нахождения всех общих делителей двух чисел  
Напишите функцию `common_divisors(a, b)`, которая принимает два числа и 
возвращает множество их общих делителей.

🔹 Пример работы:
```python
print(common_divisors(12, 18))
```

Ожидаемый результат:
```python
{1, 2, 3, 6}
```

## Task 4
Функция, которая удаляет из списка дубликаты, но сохраняет порядок  
Напишите функцию `remove_duplicates(lst)`, которая принимает список и
возвращает новый список без дубликатов, сохраняя их первый порядок появления.

🔹 Пример работы:
```python
print(remove_duplicates([4, 2, 3, 2, 4, 1, 3]))
```

Ожидаемый результат:
```python
[4, 2, 3, 1]
```

## Task 5
Функция для удаления запрещённых слов из текста  
Напишите функцию `censor_text(text, banned_words)`, которая принимает текст и 
множество запрещённых слов, возвращает текст без этих слов.

🔹 Пример работы:
```python
print(censor_text("Python — лучший язык программирования", {"лучший", "язык"}))
```

Ожидаемый результат:
```python
Python — программирования
```

## Task 6
Функция, которая проверяет, содержит ли строка все буквы алфавита  
Напишите функцию `is_pangram(text)`, которая принимает строку и возвращает True, 
если в строке встречаются все буквы английского алфавита (a-z) хотя бы раз, и False в противном случае.

🔹 Пример работы:
```python
print(is_pangram("The quick brown fox jumps over the lazy dog"))
print(is_pangram("Hello, world!"))
```

Ожидаемый результат:
```python
True
False
```
