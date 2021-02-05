

def main():

    #create empty lists and dictionaries
    teamWins = {}
    yearWin = {}
    teamNames = []

    #open file
    winnersText = open("WorldSeriesWinners.txt")

    #read first line of file
    line = winnersText.readline()
    line = line.rstrip()

    #writing teams to list
    while line != '':
        teamNames.append(line)
        line = winnersText.readline()
        line = line.rstrip()

    winnersText.close()

    #team wins dictionary
        #establish keys
    for name in teamNames:
        teamWins[name] = 0

        #giving keys their values
    for name in teamNames:
        teamWins[name] += 1

    #year win dictionary
    year = 1903
    yearWin[1994] = "(World Series Not Played This Year)"
    yearWin[1904] = "(World Series Not Played This Year)"

    for name in teamNames:
        if year == 1904 or year == 1994:
            year += 1
            yearWin[year] = name
            year += 1
        else:
            yearWin[year] = name
            year += 1

    #user input and display
    year = input("Please enter a year between 1903 and 2009")

    if year in range (1903,2009):
        print("In ", year, ", the ", yearWin[year], " won. This team had won ", teamWins[year], " World Series.")
    else:
        while year > 2009 or year < 1903:
            input("Please enter a year within 1903 and 2009")
    
main()