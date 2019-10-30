
# coding: latin-1

# In[1]:

import markovify
import pandas as pd
import nltk

# Extract text from csv; put into string
debate_csv = pd.read_csv("./assets/debate.csv", encoding='latin-1')
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

    return_banter = ""

    if short_sentence:
        short_clinton = markov_clinton.make_short_sentence(sentence_size)
        short_trump = markov_trump.make_short_sentence(sentence_size)

        return_banter += "Clinton: " + short_clinton + "<br>" + "Trump: " + short_trump + "<br>"

    else:
        clinton = markov_clinton.make_sentence()
        trump = markov_trump.make_sentence()

        return_banter += "Clinton: " + short_clinton + "<br>" + "Trump: " + short_trump + "<br>"

    return return_banter

def banter(num_lines, short_sentence = True, sentence_size = 140, **kwargs):
    topics = kwargs.get('topics')
    return_banter = ""

    if topics:
        for topic in topics:
            print ("Round Topic: {0}").format(topic)
            for i in range(num_lines):
                banter = str(generate_banter(short_sentence, sentence_size))
                return_banter += banter + "<br>"
    else:
        for i in range(num_lines):
                banter = str(generate_banter(short_sentence, sentence_size))
                return_banter += banter

    return ("<br>" + return_banter)


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
