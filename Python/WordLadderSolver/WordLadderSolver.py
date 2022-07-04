import sys
firstWord = input("Enter the starting word: ").upper()
lastWord = input("Enter the final word: ").upper()
allWords = []
with open("4-letter-words.txt", 'r') as file:
    for line in file:
        allWords.append(line[:-1])
global shortestDepth
shortestDepth = 10

def editString(string,lastWord, route, allWords, depth=0):
    route.append(string)
    depth+=1
    global shortestDepth
    if (depth < shortestDepth):
        same=0
        for i in range(4):
            if (string[i]==lastWord[i]):
                same+=1
        if same==3:
            print(route, depth)
            shortestDepth = depth
            route.pop()
            return;
        
        for character in 'abcdefghijklmnopqrstuvwxyz'.upper():
            currentString = character + string[1:]
            if (currentString not in route):
                if (currentString in allWords):
                    editString(currentString, lastWord, route,allWords, depth)
            currentString = string[:1] + character + string[2:]
            if (currentString not in route):
                if (currentString in allWords):
                    editString(currentString, lastWord, route,allWords, depth)
                currentString = string[:2] + character + string[3:]
            if (currentString not in route):
                if (currentString in allWords):
                    editString(currentString, lastWord, route,allWords, depth)
            currentString = string[:3] + character
            if (currentString not in route):
                if (currentString in allWords):
                    editString(currentString, lastWord, route,allWords, depth)
    route.pop()

sys.setrecursionlimit(shortestDepth)
print(shortestDepth)
steps = []
editString(firstWord, lastWord, steps, allWords)
