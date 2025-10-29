import re
from collections import Counter

def is_palindrome(word):
    word = word.replace(' ', '').lower()
    return True if word == word[::-1] else False

def fibonacci(v: int):
    if v < 0:
        raise ValueError("n musi byc liczba nieujemna")

    if v == 0:
        return 0
     
    if v == 1:
        return 1
     
    a, b = 0, 1
    for _ in range(2, v + 1):
        a, b = b, a + b

    return b

def count_vowels(text: str) -> int:
    vowels = "aeiouyółAEIOUYÓŁ"
    return sum(1 for c in text if c in vowels)

def calculate_discount(price: float, discount: float):
    if price < 0 or discount < 0 or discount > 1:
        raise ValueError("Niepoprawna wartość")
    return price * (1 - discount)
    
def flatten_list(nested_list):
    flat = []
    for item in nested_list:
        if isinstance(item, list):
            flat.extend(flatten_list(item))
        else:
            flat.append(item)
    return flat

def word_frequencies(text: str):
    words = re.findall(r'\b[a-z]+\b', text.lower())
    return dict(Counter(words))

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
