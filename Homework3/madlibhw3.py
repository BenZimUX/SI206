# Using text2 from the nltk book corpa, create your own version of the
# MadLib program.  

# Requirements:
# 1) Only use the first 150 tokens
# 2) Pick 5 parts of speech to prompt for, including nouns
#      - Nouns, Adjective, Verbs, Adverb, Plural Nouns
# 3) Replace nouns 15% of the time, everything else 10%

# Deliverables:
# 1) Print the orginal text (150 tokens)
# 1) Print the new text
print("***Start***")

import nltk 
from nltk.book import text2
import random 


tokens = text2[:151]
print ("\n")
print("***First 150 Tokens***")
print(tokens)

tagged_tokens = nltk.pos_tag(tokens) # gives us a tagged list of tuples
tagged_tokens = tagged_tokens[:151] #first 150 tokens only

print("\n")

tagmap = {"NN":"a noun","NNS":"a plural noun","VB":"a verb","JJ":"an adjective", "RB": "an adverb"}
substitution_probabilities = {"NN":.15,"NNS":.15,"VB":.10,"JJ":.10, "RB":.10}

def spaced(word): #puts spaces into each element of final_words, but makes sure there is no space between words and punctuation
	if word in [",", ".", "?", "!", ":", "[", "]"]:
		return word
	else:
		return " " + word 

final_words = []


for (word, tag) in tagged_tokens:
	if tag not in substitution_probabilities or random.random() > substitution_probabilities[tag]: #only one of these has to hold
		final_words.append(spaced(word))
	else:
		new_word = input("Please enter %s:\n" % (tagmap[tag]))
		final_words.append(spaced(new_word))

print ("\n***Your Madlib Below***")
print("\n")
print ("".join(final_words)) #gives us our completed madlib

print("\n***End***")
