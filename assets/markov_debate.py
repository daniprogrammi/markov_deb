####################################################################
####################################################################
####################################################################
# Danielle Williams -- Exploring text generation using markov chains
# * ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ * #
# You can read the accompanying blog post at danicodes.github.io   #
# This code is live at https://markov-app.herokuapp.com/           #
####################################################################
####################################################################
####################################################################

import sys
import markovify
import pandas as pd
import nltk

nltk.data.path.append('./nltk_data/') # Resolving Heroku issue, should look for any missing corpus under this path, and hopefully not crash


# Extract text from csv; put into string

class Debate:
    """

    Generate debates between two speakers

    """
    def __init__(self, speaker1, speaker2):
        """
        Initialize a debate

        :param speaker1: str, name of speaker
        :param speaker2: str, name of speaker

        """
        self.speaker1 = speaker1
        self.speaker2 = speaker2

        self.debate_csv = pd.read_csv("./assets/debate.csv", encoding='latin-1')

        # Model created on initialization to speed up calling generate banter
        self.speaker1_model = self._markovify_speaker(speaker1)
        self.speaker2_model = self._markovify_speaker(speaker2)

    def _markovify_speaker(self, speaker):
        """
        extract a speaker's text from debate.csv and return a markovified model
        :param speaker: str, name of speaker as it appears in csv asset
        :return: markofivy model
        """
        speaker_corpus = self.debate_csv[self.debate_csv["Speaker"] == speaker]["Text"]
        speaker_string = " ".join(speaker_corpus)
        markovify_speaker_model = markovify.Text(speaker_string)

        return markovify_speaker_model

    def generate_banter(self, short_sentence=True, sentence_size=140):
        """
        generate a line between each speaker

        :param short_sentence: bool, default True, if true will opt to make short sentences
        :param sentence_size: int, maximum number characters in a sentence
        :return: str, banter
        """
        return_banter = ""

        if short_sentence:
            short_speaker1 = self.speaker1_model.make_short_sentence(sentence_size)
            short_speaker2 = self.speaker2_model.make_short_sentence(sentence_size)

            return_banter += "{}: {} \n".format(self.speaker1, short_speaker1) + \
                             "{}: {} \n".format(self.speaker2, short_speaker2)

        else:
            reg_speaker1 = self.speaker1_model.make_sentence()
            reg_speaker2 = self.speaker2_model.make_sentence()

            return_banter += "{}: {} \n".format(self.speaker1, reg_speaker1) + \
                             "{}: {} \n".format(self.speaker2, reg_speaker2)

        return return_banter

    def banter(self, num_lines, short_sentence=True, sentence_size=140, **kwargs):
        """
        banter generates a series of lines between two speakers by calling generate_banter for
        <num_lines> times

        :param num_lines: int, number of statements to generate for each speaker
        :param short_sentence: bool, default True, if true will opt to make short sentences
        :param sentence_size: int, maximum number characters in a sentence
        :return str, banter

        Todo: Generate rebuttal based on topic/s from previous sentence for semblance of flow
        Extract nouns/get rid of closed-class words from first generated sentence;
        Generate next sentence (rebuttal) based on nouns/topics from previous;
        """
        topics = kwargs.get('topics')

        def create_banter(num_lines, short_sentence, sentence_size):
            return_banter = ""
            for i in range(num_lines):
                banter = str(self.generate_banter(short_sentence, sentence_size))
                return_banter += banter + "\n"

            return return_banter

        # TODO: Edit banter to accept topics
        if topics:
            for topic in topics:
                print("Round Topic: {}".format(topic))
                return create_banter(num_lines, short_sentence, sentence_size)

        else:
            return create_banter(num_lines, short_sentence, sentence_size)


# Example usage
def main():
    new_debate = Debate("Clinton", "Trump")

    while True:
        print("Type e to exit")
        num_lines_in_banter = input("How many lines of banter should be generated?: ")

        if str(num_lines_in_banter) == 'e':
            break

        print("\n\n Your Debate: \n")
        print(new_debate.banter(int(num_lines_in_banter)))

    return


if __name__ == "__main__":
    main()
    sys.exit(0)
