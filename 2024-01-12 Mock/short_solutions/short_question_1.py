def extractText(text: str, keys: str) -> str:
    return (lambda keys: " ".join(list(filter(lambda word: all(map(lambda letter: letter in keys, word.lower())), text.split(" ")))))(keys.lower())
