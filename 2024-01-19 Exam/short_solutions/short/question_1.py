def string_pattern(size: int) -> str:
    return "".join(list(map(lambda line_num: f'{"".join(list(map(lambda char_pos: "+" if char_pos == line_num or char_pos == size - line_num - 1 else "-", range(size))))}\n', range(size)))) if size > 2 else exec('raise ValueError("Size given was too small")')
