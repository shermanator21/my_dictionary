def main():
    infile = open("book of John text.txt", "r")

    # read in file text to line, convert to string, and split string
    line = infile.readlines()
    line = str(line)
    line = line.split()

    # create variable counts
    FatherCount = 0
    GodCount = 0
    ChristCount = 0
    SpiritCount = 0
    spiritCount = 0
    lifeCount = 0
    manCount = 0

    # iterate through each word and check for word matches
    for word in line:
        if word == "Father":
            FatherCount += 1
        elif word == "God":
            GodCount += 1
        elif word == "Christ":
            ChristCount += 1
        elif word == "Spirit":
            SpiritCount += 1
        elif word == "spirit":
            spiritCount += 1
        elif word == "life":
            lifeCount += 1
        elif word == "man":
            manCount += 1

    # Display word counts
    print(
        "Father:",
        FatherCount,
        "\nGod:",
        GodCount,
        "\nChrist:",
        ChristCount,
        "\nSpirit:",
        SpiritCount,
        "\nspirit:",
        spiritCount,
        "\nlife:",
        lifeCount,
        "\nman:",
        manCount,
    )


main()