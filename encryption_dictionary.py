def main():
    codes = {
        "A": "%",
        "a": "9",
        "B": "@",
        "b": "5",
        "C": "1",
        "c": "2",
        "D": "9",
        "d": "3",
        "E": "8",
        "e": "4",
        "F": "7",
        "f": "5",
        "G": "6",
        "g": "q",
        "H": "w",
        "h": "e",
        "I": "r",
        "i": "t",
        "J": "y",
        "j": "u",
        "K": "i",
        "k": "o",
        "L": "p",
        "l": "a",
        "M": "s",
        "m": "d",
        "N": "R",
        "n": "f",
        "O": "g",
        "o": "h",
        "P": "j",
        "p": "k",
        "Q": "l",
        "q": "z",
        "R": "x",
        "r": "c",
        "S": "v",
        "s": "b",
        "T": "n",
        "t": "m",
        "U": "<",
        "u": "?",
        "V": "^",
        "v": "*",
        "W": "$",
        "w": ")",
        "X": "!",
        "x": "*",
        "Y": "&",
        "y": ";",
        "Z": "|",
        "z": "[",
        " ": "H",
        ".": "P",
        ":": "Q",
    }

    infile = open("info_security.txt", "r")
    outfile = open("encrypted_info_security.txt", "w")

    line = infile.readline()

    for i in line:
        outfile.write(codes[i])

    infile.close()
    outfile.close()


main()