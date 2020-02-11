ALPHABET = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z"]

INDEX = {}
# initialisation of INDEX
for (a, b) in zip(ALPHABET, range(0, 27)):
    INDEX[a] = b
