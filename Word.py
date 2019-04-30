import copy

allowedCharacters = "abcdefghijklmnopqrstuvwxyz"

class Word:

    def __init__(self, word):
        self.word = str.lower(word)
        self.createCharacterMap()
        self.sortTuples()

    # create a charmap counting all relevant chars
    def createCharacterMap(self):
        charMap = {}
        for character in self.word:
            if character not in allowedCharacters: continue
            if character in charMap:
                charMap[character] += 1
            else:
                charMap[character] = 1
        self.characterMap = charMap

    # create sorted tuples
    def sortTuples(self):
        listTuples = [(key, self.characterMap[key]) for key in self.characterMap.keys()]
        self.length = len(listTuples)
        self.sortedTuples = sorted(listTuples)

    # compares two word objects
    def compare(self, targetWord):
        myWordChars = self.characterMap.keys()
        myWordCharsLength = len(myWordChars)
        targetWordChars = targetWord.characterMap.keys()
        targetWordCharsLength = len(targetWordChars)
        isPerfectMatch = True
        if myWordCharsLength > targetWordCharsLength: return -1
        for char in myWordChars:
            if char not in targetWordChars: return -1
            if self.characterMap[char] > targetWord.characterMap[char]: return -1
            if self.characterMap[char] < targetWord.characterMap[char]: isPerfectMatch = False
        if myWordCharsLength < targetWordCharsLength: isPerfectMatch = False
        return 0 if isPerfectMatch else 1

    # Merges two words together to a new word
    def mergeWords(self, otherWord):
        thisWord = copy.deepcopy(self)
        thisWord.word += " " + otherWord.word
        thisWord.characterMap = self.mergeMaps(thisWord.characterMap, otherWord.characterMap)
        thisWord.sortTuples()
        return thisWord

    # Merges two maps together
    def mergeMaps(self, charMap1, charMap2):
        for key in charMap2.keys():
            if key in charMap1:
                charMap1[key] += charMap2[key]
            else:
                charMap1[key] = charMap2[key]

        return charMap1
