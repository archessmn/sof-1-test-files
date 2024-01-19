def shrink(signal: list[int], element: list[int]) -> list[int]:
    return list(map(lambda bit_position: (lambda slices: 1 if slices[0] == slices[1] else 0)((signal[bit_position:], element[: len(signal) - bit_position]) if bit_position + len(element) > len(signal) else (signal[bit_position: bit_position + len(element)], element)), range(len(signal))))


def expand(signal: list[int], element: list[int]) -> list[int]:
    return list(map(lambda bit_position: (lambda slices: 1 if any(signal_bit in slices[1] for signal_bit in slices[0]) else 0)((signal[bit_position:], element[: len(signal) - bit_position]) if bit_position + len(element) > len(signal) else (signal[bit_position: bit_position + len(element)], element)), range(len(signal))))


def denoise(signal: list[int], element: list[int]) -> list[int]:
    return expand(shrink(signal, element), element)


signal = [1, 0, 0, 1, 0, 0, 1, 1, 0, 1]
structuring_element = [1, 1]
print(shrink(signal, structuring_element) == [0, 0, 0, 0, 0, 0, 1, 0, 0, 1])
print(expand(signal, structuring_element) == [1, 0, 1, 1, 0, 1, 1, 1, 1, 1])
print(denoise(signal, structuring_element) == [0, 0, 0, 0, 0, 1, 1, 0, 1, 1])
