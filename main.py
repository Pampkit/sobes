import os
import re
from collections import Counter


def prime_numbers(low, high):
    def is_prime(number):
        if number <= 1:
            return False
        if number <= 3:
            return True
        if number % 2 == 0 or number % 3 == 0:
            return False
        i = 5
        while i * i <= number:
            if number % i == 0 or number % (i + 2) == 0:
                return False
            i += 6
        return True

    if not (isinstance(low, int)) or not (isinstance(high, int)):
        return []
    if low > high or low < 0 or high < 0:
        return []

    primes = []
    for num in range(low, high + 1):
        if is_prime(num):
            primes.append(num)

    return primes


def text_stat(filename):
    if not (isinstance(filename, str)) or not (
            os.path.exists(filename)):  # Проверка данных
        return {"error": "Некорректное имя файла"}

    with open(filename, "r", encoding='utf-8') as f:
        text = f.read()

    text = re.sub(r"[#%!@*-]", "", text).lower()
    words = re.findall(r'\b[\wа-яА-ЯёЁ]+\b', text)  # все слова
    letters = [char for char in text if char.isalpha()]  # все буквы

    letter_counts = dict(Counter(letters))  # dict буква:количество в тексте
    letter_counts = dict(sorted(letter_counts.items()))
    word_count = len(words)  # Кол-во слов
    paragraph_count = text.count('\n\n') + 1  # Кол-во параграфов

    bilingual_word_count = sum(1 for word in words if  # Кол-во слов из обоих алфавитов
                               any(char in 'abcdefghijklmnopqrstuvwxyz' for char in word) and any(
                                   char in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя' for char in word))
    letter_frequency = {}

    for letter, count in letter_counts.items():
        word_count_with_letter = sum(1 for word in words if letter in word)
        letter_frequency[letter] = (count / len(letters), word_count_with_letter / word_count)

    result = {
        "letter_frequency": letter_frequency,
        "word_amount": word_count,
        "paragraph_amount": paragraph_count,
        "bilingual_word_amount": bilingual_word_count
    }

    return result


def roman_numerals_to_int(roman_numeral):
    if not (isinstance(roman_numeral, str)):
        return None
    pattern = re.compile(r"""
                                    ^M{0,3}
                                    (CM|CD|D?C{0,3})?
                                    (XC|XL|L?X{0,3})?
                                    (IX|IV|V?I{0,3})?$
                """, re.VERBOSE)

    r_list = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for i in roman_numeral:
        if i not in r_list.keys() or not (re.match(pattern, roman_numeral)):
            return None
    last_char = roman_numeral[-1]
    result = r_list[last_char]
    check_si = 0
    for i in roman_numeral[-2::-1]:
        if r_list[i] >= r_list[last_char]:
            result += r_list[i]
        else:
            check_si += 1
            result -= r_list[i]
        last_char = i
    return result



