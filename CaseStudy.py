"""
This program computes the number of sentences in a txt file.
Sentences ending in "!" and "?" are not taken care of.
"""

import os
vowels = "aeiouAEIOU"
syllables = 0
wordCount = 0
sentencesCount = 0
index = float(0)

# opening the correct file in the directory
myDirectory = os.getcwd()
filenames = os.listdir(myDirectory)
entered = input("Enter your file name: ")


for files in filenames:
    if entered == files:
        f = open(entered, newline='\n')
# Seperate on periods to get sentences.
        for lines in f:
            sentences = lines.split(".")
# Seperate on spaces to get words.
            for words in sentences:
                wordsList = words.split(" ")
# Count the syllables
                for word in wordsList:
                    for vowel in vowels:
                        syllables = syllables + word.count(vowel)
                    for ending in ['es', 'ed', 'e']:
                        if word.endswith(ending):
                            syllables = syllables - 1
                    if word.endswith("le"):
                        syllables += 1

        break
    elif entered != files:
        continue
if entered not in filenames:
    print("There is no such file on the current working directory")

# Count number of sentences
file = open(entered, newline='\n')
text = file.read()
sentencesCount = text.count(".")
# Count number of words
wordCount = len(text.split())


# Compute the Flesch Index and Grade Level
index = 206.835 - 1.015 * (wordCount / sentencesCount) - \
                           84.6 * (syllables / wordCount)
level = round(0.39 * (wordCount / sentencesCount)
              + 11.8 * (syllables / wordCount) - 15.59)

print("This text is comprised of %d syllables, %d words, and %d sentences" %
      (syllables, wordCount, sentencesCount))
print("The Flesh index is %d" % index)
print("The Grade level is %d" % level)
