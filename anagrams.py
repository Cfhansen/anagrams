def readfile():
    file = open('anagrams\dict.txt')
    words = []
    for line in file:
        words.append(line)
    file.close()
    return words

def check(word1,word2):
    if (sorted(word1) == sorted(word2.rstrip())):
        return True
    else:
        return False

array = readfile()
word = input("Enter a word: ")
for i in range(len(array)):
    if (check(word,array[i])):
        print(array[i])
