longest_palindromic_numbers = lambda number: longest_palindromic_numbers(number[1:]) if number.startswith("0") and number != "0" else {number} if number == number[::-1] else (lambda r, l: r.union(l) if len(list(r)[0]) == len(list(l)[0]) else r if len(list(r)[0]) > len(list(l)[0]) else l)(longest_palindromic_numbers(number[1:]), longest_palindromic_numbers(number[:-1]))

# r = palindromes_right
# l = palindromes_left