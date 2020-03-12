"""

Author: Saimon
"""
import pickle
import os
from bltk.langtools.taggertools import features


class PosTagger:
    def __init__(self):
        self.data = PosTagger.get_data()

    @staticmethod
    def get_data():
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..//data//pos_tagger.pkl"), "rb") as tagger:
            pos_tagger = pickle.load(tagger)
            return pos_tagger

    def pos_tag(self, sentence: list):
        the_tags = self.data.predict([features(sentence, index) for index in range(len(sentence))])
        return list(zip(sentence, the_tags))
