
# coding: utf-8

# In[1]:

import markovify
import pandas as pd
import nltk

# Extract text from csv; put into string
debate_csv = pd.read_csv("./assets/debate.csv")
debate_clinton = debate_csv[debate_csv["Speaker"] == "Clinton"]["Text"]
debate_trump = debate_csv[debate_csv["Speaker"] == "Trump"]["Text"]

clinton_text = ""
for line in debate_clinton:
    clinton_text += line

trump_text = ""
for line in debate_trump:
    trump_text += line

# Create markov chains from the texts
markov_clinton = markovify.Text(clinton_text)
markov_trump = markovify.Text(trump_text)


# If topics are present:
#     For each topic generate sentence based on the topic
#     Generate rebutal based on topic/s from previous
#     Follow general sentence flow
# If topics are present:
#     num_lines will be number of lines of debate for EACH topic
#
# GENERAL for sentence flow -
# Extract nouns/get rid of closed-class words from first generated sentence; Generate next sentence (rebuttal) based on nouns/topics from previous; 16
#
#
#

# In[4]:

def generate_banter(short_sentence = True, sentence_size = 140):

    if short_sentence:
        short_clinton = markov_clinton.make_short_sentence(sentence_size)
        short_trump = markov_trump.make_short_sentence(sentence_size)
        print ("Clinton: {0}").format(short_clinton)
        print("Trump: {0}").format(short_trump)

        print("\n")
    else:
        clinton = markov_clinton.make_sentence()
        trump = markov_trump.make_sentence()

        print ("Clinton: {0}").format(clinton)
        print("Trump: {0}").format(trump)

        print ("\n")

def banter(num_lines, short_sentence = True, sentence_size = 140, **kwargs):
    topics = kwargs.get('topics')
    if topics:
        for topic in topics:
            print ("Round Topic: {0}").format(topic)

            for i in range(num_lines):
                generate_banter(short_sentence, sentence_size)
    else:
        for i in range(num_lines):
                generate_banter(short_sentence, sentence_size)


#""" MODULE CHANGE
#def make_sentence_including(words):

#"""




# In[6]:

#banter(1, topics = ["Race", "Grace", "Mace"])

sentence = markov_clinton.make_sentence()
test = nltk.word_tokenize(sentence)

#nltk.pos_tag(sentence)

#nltk.word_tokenize() nltk.tokenize()




# In[ ]:
