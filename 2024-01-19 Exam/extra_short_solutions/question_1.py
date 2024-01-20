string_pattern = lambda s: "".join(list(map(lambda l: f'{"".join(list(map(lambda c: "+" if c == l or c == s - l - 1 else "-", range(s))))}\n', range(s)))) if s > 2 else exec('raise ValueError()')

# s = size
# l = line_num
# c = char_pos