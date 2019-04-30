from Word import Word

# global scope variables
fileName = "wordlist"
targetWord = Word("poultry outwits ants")
#targetWord = Word("abdication")

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
        iterateThrough(content[i], 0, wordAmount, content)

def iterateThrough(word, startPos, totalLength, contentList):
    for i in range(startPos, totalLength):
        compareCode = word.compare(targetWord)
        if compareCode == -1: break
        if compareCode == 0: print(word.word)
        if compareCode == 1 and i < totalLength - 1:
            iterateThrough(word.mergeWords(contentList[i + 1]), i + 1, totalLength, contentList)

# Main function... Got the action.. and the bitches
def main():
    content = fileReader()
    content = [Word(str) for str in content]
    findMatches(content)

def test():
    print(Word("a").compare(Word("fo")))

if __name__ == "__main__": main()