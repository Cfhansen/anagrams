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

def anagram_list(word):
    array = readfile()
    anagram_array = []
    for i in range(len(array)):
        if (check(word,array[i])):
            anagram_array.append(array[i].rstrip())
    return anagram_array

def guess(array):
    g = input("Guess an anagram! Press ` to quit. ")
    if (g == "`"):
        print("You gave up! Here's the list of anagrams:")
        print(array)
        return
    else:
        if (g in array):
            print("That's right!")
            array.remove(g)
            if (len(array) == 0):
                print("You guessed all possible anagrams!")
            else:
                guess(array)
        else:
            print("That's not a valid anagram.")
            guess(array)

word = input("Enter a word: ")
array = anagram_list(word)
print("This word has " + str(len(array)) + " anagrams.")
guess(array)
