# Ocana - lexer
import sys

filename = sys.argv[1]

with open(filename) as f:
    source = f.read()

# Symbols that are one character long
SYMBOLS = {
    "=": "EQUAL",
    "+": "PLUS",
    "-": "MINUS",
    "*": "STAR",
    "/": "SLASH",
    "(": "LPAREN",
    ")": "RPAREN",
}
# Look at each character, one by one
pos = 0
while pos < len(source):
    char = source[pos]
    if char in SYMBOLS:
        print(SYMBOLS[char], char)
    elif char == " " or char == "\n":
        pass  # skip spaces and new lines
    elif char.isdigit():
        start = pos
        while pos < len(source) and source[pos].isdigit():
            pos = pos + 1
        print("NUMBER", source[start:pos])
        continue  # pos already moved, go back to the top
    elif char.isalpha() or char == "_":
        start = pos
        while pos < len(source) and (source[pos].isalnum() or source[pos] == "_"):
            pos = pos + 1
        print("NAME", source[start:pos])
        continue  # pos already moved, go back to the top
    elif char == '"':
        pos = pos + 1  # skip the opening quote
        start = pos
        while pos < len(source) and source[pos] != '"':
            pos = pos + 1
        print("STRING", source[start:pos])
    else:
        print("UNKNOWN", char)
    pos = pos + 1
