from src import *
import pytest

class TestPalindrome:
    def test_is_palindrome_kajak(self):
        assert is_palindrome("kajak") == True

    def test_is_palindrome_kobyla_ma_maly_bok(self):
        assert is_palindrome("Kobyła ma mały bok") == True

    def test_is_palindrome_python(self):
        assert is_palindrome("python") == False

    def test_is_palindrome_(self):
        assert is_palindrome("") == True

    def test_is_palindrome_A(self):
        assert is_palindrome("A") == True

class TestFibonacci:
    def test_is_fibonacci_0(self):
        assert fibonacci(0) == 0

    def test_is_fibonacci_1(self):
        assert fibonacci(1) == 1

    def test_is_fibonacci_5(self):
        assert fibonacci(5) == 5

    def test_is_fibonacci_10(self):
        assert fibonacci(10) == 55

    def test_is_fibonacci_minus_1(self):
        with pytest.raises(ValueError):
            fibonacci(-1)

class TestCountVowels:
    def test_count_vowels_Python(self):
        assert count_vowels("Python") == 2

    def test_count_vowels_AEIOUY(self):
        assert count_vowels("AEIOUY") == 6

    def test_count_vowels_bcd(self):
        assert count_vowels("bcd") == 0

    def test_count_vowels_(self):
        assert count_vowels("") == 0

    def test_count_vowels_Proba_zolwia(self):
        assert count_vowels("Próba żółwia") == 6

class TestCalculateDiscount:
    def test_calculate_discount_100_0_2(self):
        assert calculate_discount(100,0.2) == 80.0

    def test_calculate_discount_50_0(self):
        assert calculate_discount(50,0) == 50.0

    def test_calculate_discount_200_1(self):
        assert calculate_discount(200,1) == 0.0

    def test_calculate_discount_100_minus_0_1(self):
        with pytest.raises(ValueError):
            calculate_discount(100, -0.1)
    
    def test_calculate_discount_100_1_5(self):
        with pytest.raises(ValueError):
            calculate_discount(100, 1.5)

class TestFlattenList:
    def test_flatten_list_1(self):
        assert flatten_list([1, 2, 3]) == [1, 2, 3]

    def test_flatten_list_2(self):
        assert flatten_list([1, [2, 3], [4, [5]]]) == [1, 2, 3, 4, 5]

    def test_flatten_list_3(self):
        assert flatten_list([]) == []

    def test_flatten_list_4(self):
        assert flatten_list([[1]]) == [1]

    def test_flatten_list_5(self):
        assert flatten_list([1, [2, [3, [4]]]]) == [1, 2, 3, 4]

class TestWordFrequencies:
    def test_word_frequencies_to_be(self):
        assert word_frequencies("To be or not to be") == {"to": 2, "be": 2, "or": 1, "not": 1}

    def test_word_frequencies_hello(self):
        assert word_frequencies("Hello hello!") == {"hello": 2}

    def test_word_frequencies_empty(self):
        assert word_frequencies("") == {}

    def test_word_frequencies_python(self):
        assert word_frequencies("Python python python") == {"python": 3}

    def test_word_frequencies_ala(self):
        assert word_frequencies("Ala ma kota, a kot ma Ale.") == {'ala': 1, 'ma': 2, 'kota': 1, 'kot': 1, 'a': 1, 'ale': 1}

class TestIsPrime:
    def test_is_prime_2(self):
        assert is_prime(2) == True

    def test_is_prime_3(self):
        assert is_prime(3) == True

    def test_is_prime_4(self):
        assert is_prime(4) == False

    def test_is_prime_0(self):
        assert is_prime(0) == False

    def test_is_prime_1(self):
        assert is_prime(1) == False

    def test_is_prime_5(self):
        assert is_prime(5) == True

    def test_is_prime_97(self):
        assert is_prime(97) == True