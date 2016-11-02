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
print("START*******")

import nltk 
from nltk.book import *
from nltk import bigrams
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk import word_tokenize,sent_tokenize
import random #one of these is printing all the texts, is this ok?

# print("\n\n")
# print("type of text 2 is ", type(text2))
# print("Length of ",text2,"is",len(text2))
# print("Unique tokens in",text2,"are: ",len(set(text2)))

debug = False #True

# get file from user to make mad lib out of
if debug:
	print ("Getting information from file madlib_test.txt...\n")

fname = "austen-sense.txt"


f = open(fname, 'r')
para = f.read()
tokens = nltk.word_tokenize(para)
#print("TOKENS")
#print(tokens[:151])
tagged_tokens = nltk.pos_tag(tokens) # gives us a tagged list of tuples
#print("TAGGED TOKENS")
#print(tagged_tokens[:151])
if debug:
	print ("First few tagged tokens are:")
	for tup in tagged_tokens[:151]:
		print (tup)

tagmap = {"NN":"a noun","NNS":"a plural noun","VB":"a verb","JJ":"an adjective", "ADV": "an adverb"}
substitution_probabilities = {"NN":.15,"NNS":.15,"VB":.10,"JJ":.10}

def spaced(word):
	if word in [",", ".", "?", "!", ":"]:
		return word
	else:
		return " " + word

final_words = []


for (word, tag) in tagged_tokens:
	if tag not in substitution_probabilities or random.random() > substitution_probabilities[tag]:
		final_words.append(spaced(word))
	else:
		new_word = input("Please enter %s:\n" % (tagmap[tag]))
		final_words.append(spaced(new_word))

print ("".join(final_words))


# sentences = sent_tokenize(text2)
# print ("Type of sentences is", type(sentences))
print("\n\n")






# for i in sentences:
# 	print(i)

print("\n\nEND*******")
