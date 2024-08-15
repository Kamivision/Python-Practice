# In sololearn code coach
# Take a sentence in english and turn it into pig latin
# input should be a string with no capitalization or punctuation
# output should be the same sentence in piglatin with the first letter at theend followed by ay 

#take a sentence as input w/o capitalization or punctuation
#english_sentence = "well that happened"
english_sentence = input("Please enter a sentence with no capitalization or punctuation: ")


def pig_latin():
# split the inputted string into a list of words
    words = english_sentence.split()

 # move initial consonant to the end
    move_initial = []

    for w in words:
        move_initial.append(w[1: ] + w[0])

     # add 'ay'
    latinized = []

    for w in move_initial:
        latinized.append(w + 'ay')

    new_sentence = " ".join(latinized)

    return new_sentence
    #output new sentence
      
print("The sentence in pig latin is... " + pig_latin())
