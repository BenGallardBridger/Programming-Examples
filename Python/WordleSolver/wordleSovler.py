import random

#Get the arrays to contain the letters in, not in and in place
def letterResult(guess, Result):
    lettersInPlace = {} # Dictionary to contain [letter, index] [Key, value]
    lettersInWord = []
    lettersNotInWord = []
    #adds letters to their array
    for index in range(0,5):
        if Result[index] == 'g':
            lettersInPlace[guess[index]] = index
        elif Result[index] == 'y':
            lettersInWord.append(guess[index])
        else:
            lettersNotInWord.append(guess[index])
    return lettersInPlace, lettersInWord, lettersNotInWord

#Filter the words list to not contain the letters in the list
def wordsWithout(wordList, withoutList):
    newList = [] 
    for word in wordList: # Checks every word
        isGood = True
        for letter in withoutList: # Checks every letter
            if letter in word:
                isGood = False
        if isGood: # If no invalid check, add to new list
            newList.append(word)
    return newList

#
def wordLetterAt(wordList, letterInd):
    newList = []
    for word in wordList:
        isGood = True
        for key in letterInd:
            value = letterInd[key]
            try:
                if word[value] != key:
                    isGood = False
            except:
                print(value)
                IndexError
        if isGood:
            newList.append(word)
    return newList

def wordWith(wordList, letters):
    newList = []
    for word in wordList:
        isGood = True
        for letter in letters:
            if letter not in word:
                isGood = False
        if isGood:
            newList.append(word)
    return newList

def calculateLetterFreq(wordList):
    letters = {}
    for word in wordList:
        for letter in word:
            try:
                letters[letter] +=1
            except:
                letters[letter] = 1
    return letters

def makeGuess1(currentWord, wordList, letterDict):
    mostLikelyWord = ""
    liklihood = 0
    for word in wordList:
        likely = 0
        for key in letterDict:
            value = letterDict[key]
            if key in word:
                likely += value
        if liklihood < likely:
            mostLikelyWord = word
            liklihood = likely
    guessResult = []
    counter = 0
    for index in range(0,5):
        if currentWord[index] == mostLikelyWord[index]:
            guessResult.append('g')
        elif mostLikelyWord[index] in currentWord:
            guessResult.append('y')
        else:
            guessResult.append('n')
    return mostLikelyWord, guessResult

def makeGuess2(wordList, letterDict):
    mostLikelyWord = ""
    liklihood = 0
    for word in wordList:
        likely = 0
        for key in letterDict:
            value = letterDict[key]
            if key in word:
                likely += value
        if liklihood < likely:
            mostLikelyWord = word
            liklihood = likely
    return mostLikelyWord

def makeGuess3(index):
    arr = ['brick', 'jumpy', 'vozhd', 'glent', 'waqfs']
    return arr[index]

options = int(input("Enter the options: "))
if options == 0:
    accuracy = 0
    fails = 0
    for i in range(0,1000):
        words = []
        letters = {}
        with open("words.txt", 'r') as file:
            for line in file:
                words.append(line[:-1])
                for letter in line[:-1]:
                    try:
                        letters[letter] +=1
                    except:
                        letters[letter] = 1
        word = words[random.randint(0,len(words)-1)]
        print(word)
        for i in range(0,6):
            guess, result = makeGuess1(word, words, letters)
            print(f"Guess: {guess}")
            print(f"Result: {result}")
            if result.count("g") == 5:
                accuracy += i
                break
            elif i==5:
                fails+=1
                break
            atWord, inWord, notIn = letterResult(guess, result)
            words = wordsWithout(words, notIn)
            words = wordLetterAt(words, atWord)
            words = wordWith(words, inWord)
            letters = calculateLetterFreq(words)
    print(accuracy/1000)
    print(fails)
elif options==1:
    words = []
    letters = {}
    with open("words.txt", 'r') as file:
        for line in file:
            words.append(line[:-1])
            for letter in line[:-1]:
                try:
                    letters[letter] +=1
                except:
                    letters[letter] = 1
    for i in range(0,6):
        guess = makeGuess2(words,letters)
        print(f"Guess: {guess}")
        result = input("Enter result")
        if result.count("g") == 5:
            break
        atWord, inWord, notIn = letterResult(guess, result)
        words = wordsWithout(words, notIn)
        words = wordLetterAt(words, atWord)
        words = wordWith(words, inWord)
        letters = calculateLetterFreq(words)
elif options==2:
    words = []
    letters = {}
    with open("words.txt", 'r') as file:
        for line in file:
            words.append(line[:-1])
            for letter in line[:-1]:
                try:
                    letters[letter] +=1
                except:
                    letters[letter] = 1
    for i in range(0,6):
        if i == 5:
            print(makeGuess2(words, letters))
        else:
            guess = makeGuess3(i)
            print(f"Guess: {guess}")
            result = input("Enter result")
            if result.count("g") == 5:
                break
            atWord, inWord, notIn = letterResult(guess, result)
            words = wordsWithout(words, notIn)
            words = wordLetterAt(words, atWord)
            words = wordWith(words, inWord)
            letters = calculateLetterFreq(words)
