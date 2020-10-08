#Use itertools module from Python Standard Library to find permutations.
#Use sys for command line.
from itertools import permutations
from scoring import score_word
import sys

#Print error when there is only the program executed. 
if len(sys.argv) < 2:
    raise Exception("There is no rack. Please enter letters.")
    exit(1)

#Print error for wrong number of characters.
if len(sys.argv[1]) > 7 or len(sys.argv[1]) < 2:
  raise Exception("Please enter two to seven characters.")

letters = sys.argv[1].lower()

if letters.count('?') > 1 or letters.count('*') > 1:
  raise Exception("There are too many wildcards.")

with open("sowpods.txt","r") as infile:
    input_raw = infile.readlines()
    data = [datum.strip('\n') for datum in input_raw]
data = [i.lower() for i in data]

#add exceptions and raise error for non letter characters

def unique(l1): 
    list_set = set(l1) 
    unique_list = (list(list_set)) 
    return unique_list

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
valid_words = []
count = 0
length = len(letters)

while length>1:
    possible_words = unique([''.join(p) for p in permutations(letters, length)])
    for word in possible_words:
        if '?' in word and '*' in word:
            for char in alphabet:
                score = score_word(word)
                new_word = word.replace('?',char)
                for ch in alphabet:
                    new_word_2 = new_word.replace('*',ch)
                    if new_word_2 in data:
                        score_tuple = (score,new_word_2)
                        valid_words.append(score_tuple)
        elif '?' in word:
            for char in alphabet:
                score = score_word(word)
                new_word = word.replace('?',char)
                if new_word in data:
                    score_tuple = (score,new_word)
                    valid_words.append(score_tuple)
        elif '*' in word:
            for ch in alphabet:
                score = score_word(word)
                new_word = word.replace('*',ch)
                if new_word in data:
                    score_tuple = (score,new_word)
                    valid_words.append(score_tuple)
        elif word in data:
            score_tuple = (score_word(word),word)
            valid_words.append(score_tuple)
    length -= 1

valid_words = unique(valid_words)
valid_words = sorted(valid_words, key = lambda x: x[1])
valid_words = sorted(valid_words, key = lambda x: x[0], reverse = True)
count = len(valid_words)

for tup in valid_words:
    print("({}".format(tup[0])+",","{})".format(tup[1]))
    
print("Total number of words:", count)

