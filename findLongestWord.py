import math

file = open("sowpods.txt", "r")
dictionary = file.read().splitlines()
file.close()

# Obtain Words in descending length to test for their COINS quality
def findLongestCoins(dictionary):
    # We start from the longest words in the dictionary since we can stop at the first word with the COINS property
    longestWordLen = len(max(dictionary, key = len))
    longestCoins = ""
    foundLongestCoins = False

    # This while loop will check words of length longestWordLen
    while(not foundLongestCoins):
        # checkWordsByLength will only return a value when a word with the COINS property is found
        coinsWord =  checkWordsByLength(longestWordLen)
        if(coinsWord):
            longestCoins = coinsWord
            foundLongestCoins = True
        else:
            longestWordLen -= 1

    return longestCoins


def checkWordsByLength(length):
    # Obtain a list of words of a certain length
    wordsWithLengthN = list(filter(lambda x: len(x) == length, dictionary))
    print("Checking words with lenght: " + str(length))

    for word in wordsWithLengthN:
        # Check each word here for its COINS quality, if it does it will return the word
        if(checkCoins(word)):
            return word


# This function checks only a single word for its COINS property and can be used to test the checkCoins() function
def checkThisWord(word):
    if(checkCoins(word)):
        return word

# Check if a word has the COINS property
def checkCoins(word):
    # Create an array of 3 or 4 words regardless of whether they are real words

    # If the the word we are checking is only one character long, it means we have reached an "A", "I", or "O" and we have found a word
    if(len(word)<=1):
        print("found")
        # This breaks the recursion
        return True

    firstLetter = word[1:]
    lastLetter = word[:-1]
    middleLetters = removeMiddleLetters(word)

    subWords = []
    
    # Here we only populate the array of subwords if they are found in the dictionary
    if (checkWord(firstLetter)):
        subWords.append(firstLetter)
    if (checkWord(lastLetter)):
        subWords.append(lastLetter)
    for middleLetter in middleLetters:
        if (checkWord(middleLetter)):
            subWords.append(middleLetter)
    # For each valid subword, we will check its COINS property recursively until we have found one of the three one letter words        
    for subWord in subWords:
        return checkCoins(subWord)
    
# Returns an array of 3 or 4 words without the beginning, middle or last letter   
def removeMiddleLetters(word):
    subWords = []
    # Length of word
    length = len(word)

    #If the word is only 2 characters long, we do not need to remove the middle letters
    if length <=2:
        return subWords
    elif length % 2 == 1:
        middleLetter = length//2
        newWord = word[:middleLetter] + word[middleLetter+1:]
        subWords.append(newWord)
        return subWords
    else:
        middleFirst = length // 2 - 1
        middleSecond = length // 2 + 1
        middleLetterFirst = word[:middleFirst + 1] + word[middleSecond:]
        middleLetterSecond = word[:middleFirst] + word[middleSecond-1:]
        subWords.append(middleLetterFirst)
        subWords.append(middleLetterSecond)
        return subWords

# Check if a word is in the SOWDOPS dictionary        
def checkWord(word):
    return findWord(dictionary, word) != None


# Implemented a Binary search to cut down checking whether a subword is an actual word
def findWord(dictionary, word): 
    start = 0
    end = len(dictionary)
    while start < end:
        middle = start + (end - start) // 2
        midpoint = dictionary[middle]
        if word == midpoint:
            return middle
        elif word > midpoint:
            if start == middle: 
                break
            start = middle
        elif word < midpoint:
            end = middle


import time
start = time.time()
longest = findLongestCoins(dictionary)
print("Longest Word = " + longest) 
end = time.time()
print(end - start)