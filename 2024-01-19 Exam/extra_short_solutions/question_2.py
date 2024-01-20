shrink, expand, denoise = (lambda h, x: (h, x, lambda s, e: x(h(s, e), e)))(lambda s, e: list(map(lambda b: (lambda l: 1 if l[0] == l[1] else 0)((s[b:], e[: len(s) - b]) if b + len(e) > len(s) else (s[b: b + len(e)], e)), range(len(s)))), lambda s, e: list(map(lambda b: (lambda l: 1 if any(i in l[1] for i in l[0]) else 0)((s[b:], e[: len(s) - b]) if b + len(e) > len(s) else (s[b: b + len(e)], e)), range(len(s)))))

# s = signal
# e = element
# l = slices
# b = bit_position
# i = signal_bit
