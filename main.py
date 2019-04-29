
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
    def compare(self, otherWord):
        if self.length != otherWord.length: return False
        for i in range(0, self.length):
            if self.sortedTuples[i][0] != otherWord.sortedTuples[i][0] or self.sortedTuples[i][1] != otherWord.sortedTuples[i][1]:
                return False
        return True

    # todo write merge words method
    def mergeWords(self, otherWord):
        pass

# global scope variables
fileName = "wordlist"
allowedCharacters = "abcdefghijklmnopqrstuvwxyz"
#targetWord = Word("poultry outwits ants")
targetWord = Word("abdication")

# Reads the contents of the file to a list
def fileReader():
    with open(fileName) as f:
        content = f.readlines()

    content = [x.strip() for x in content]
    return content

# Finds matches
def findMatches(content):
    wordAmount = len(content)
    for i in range(0, wordAmount):
        if targetWord.compare(content[i]): print(content[i].word)


# Main function... Got the action.. and the bitches
def main():
    content = fileReader()
    content = [Word(str) for str in content]
    findMatches(content)

if __name__ == "__main__": main()