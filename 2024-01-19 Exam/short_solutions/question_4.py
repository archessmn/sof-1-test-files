def longest_palindromic_numbers(number: str) -> set[str]:
    longest_palindromic_numbers(number[1:]) if number.startswith("0") and number != "0" else {number} if number == number[::-1] else (lambda palindromes_right, palindromes_left: palindromes_right.union(palindromes_left) if len(list(palindromes_right)[
        0]) == len(list(palindromes_left)[0]) else palindromes_right if len(list(palindromes_right)[0]) > len(list(palindromes_left)[0]) else palindromes_left)(longest_palindromic_numbers(number[1:]), longest_palindromic_numbers(number[:-1]))
