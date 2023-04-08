# This script solves the NYT Spelling Bee for a set of letters
# Note: I have 0 clue how NYT actually determines the daily wordlists

MIN_WORD_LEN = 4 # NYT Spelling Bee requires words to be at least 4 letters long
NUM_LETTERS = 7 # NYT Spelling Bee words have a maximum of 7 unique letters
letter_list = ['p', 'i', 'a', 'g', 'l', 'k', 'n']
# opening a file of english words
dictFile = open('words_alpha.txt', mode='r')
dictionary = dictFile.read()
dictionary = dictionary.split('\n')
dictFile.close()

# returns the number of unique letters in a word
def numUniqueLetters(word):
    return len(set([*word]))

def isValid(word):
    return set([*word]).issubset(letter_list) and letter_list[0] in set([*word])

# removes every dictionary entry that does not meet NYT Spelling Bee reqs for length or # of unique letters
#dictionary = [word for word in dictionary if not (len(word) < MIN_WORD_LEN or numUniqueLetters(word) > NUM_LETTERS)]

dictionary = [word for word in dictionary if  len(word) > MIN_WORD_LEN and isValid(word)]

# rejoins list and writes to new file
dictionary = '\n'.join([str(word) for word in dictionary])
newDictFile = open('spellingbee_words.txt', mode='w')
newDictFile.write(dictionary)
newDictFile.close()