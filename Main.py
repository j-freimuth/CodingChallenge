from Word import Word

# global scope variables
fileName = "wordlist"
targetWord = Word("poultry outwits ants")
#targetWord = Word("abdication")
count = 0
combinationsFound = set()
percentage = 0

# Reads the contents of the file to a list
def fileReader():
  with open(fileName) as f:
    content = f.readlines()
  content = [x.strip() for x in content]
  return content

# Finds matches
def findMatches(content):
  wordAmount = len(content)
  global percentage
  for i in range(0, wordAmount):
    print(f"Word number: {i}")
    percentage = (i+1) * 100 / wordAmount
    iterateThrough(content[i], 1, wordAmount, content)
  print([w.word for w in combinationsFound])

# Iterate through the content and try all combinations
def iterateThrough(word, startPos, totalLength, contentList):
  countUp()
  for i in range(startPos, totalLength):
    compareCode = word.compare(targetWord)
    if compareCode == -1:
      break
    if compareCode == 0:
      combinationsFound.add(word.word)
      break
    if compareCode == 1 and i < totalLength - 1:
      iterateThrough(word.mergeWords(contentList[i + 1]), i + 2, totalLength, contentList)

# Count the attempts done
def countUp():
  global count
  count += 1
  if count % 100000 == 0: print(f"Attempts tried: {count}. Found: {len(combinationsFound)}, Percentage Done: {percentage}%")

# Main function...
def main():
  content = fileReader()
  content = [Word(str, targetWord) for str in content]
  print(f"Created {len(content)} words")
  content = [word for word in content if word.isValid]
  print(f"Reduced to {len(content)} valid candidates.")
  findMatches(content)

def test():
  print(Word("a").compare(Word("fo")))

if __name__ == "__main__": main()