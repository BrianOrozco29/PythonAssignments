def longestWord(inFile, outFile):
    inF = open(inFile, 'r')
    outF = open(outFile, 'w')

    for line in inF:
        wordList = line.split()
        if len(wordList) == 0:
            continue
                      
        longestLength = 0
        for word in wordList:
            length = len(word)
            if length > longestLength:       
                longestLength = length
        outF.write(str(longestLength) + "\n")
    outF.close()

longestWord("trouble.txt", "trouble_out.txt")
