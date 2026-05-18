trick_score = lambda t, r: (lambda a, s: exec('raise ValueError()') if len(t) != 4 or any(c[1] not in s for c in t) or any(c[0] not in a for c in t) else exec('raise TypeError("Invalid suit provided")') if r not in s else sum(map(lambda n: a[n[0]][0] if n[1] == r else a[n[0]][-1], t)))({"7": [0], "8": [0], "9": [14, 0], "10": [10], "Jack": [20, 2], "Queen": [3], "King": [4], "Ace": [11]}, {"Spades ", "Diamonds", "Hearts", "Clubs"})

# t = trick
# r = trump_suit
# a = ranks
# s = suits
# c = card
# n = rank_suit