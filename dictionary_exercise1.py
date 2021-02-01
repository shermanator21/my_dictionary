def main():
    textFile = open("text.txt")
    dict = {}
    textList = []
    line = textFile.readline()

#writing text file to list
    while line != '':
        line = line.split()
        for word in line:
            textList.append(word)
        line = textFile.readline()

#iterating through each word and counting
    for word in textList:
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1
    textFile.close()
    print dict

main()