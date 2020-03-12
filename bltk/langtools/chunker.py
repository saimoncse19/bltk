from nltk import RegexpParser
from bltk.langtools.pos_tagger import PosTagger


class Chunker:

    def __init__(self, grammar: str, tokened_text: list):
        self.grammar = grammar
        self.texts = tokened_text
        self.pos_tagger = PosTagger()

    def chunk(self):
        parser = RegexpParser(self.grammar)

        sentence_tagged = self.pos_tagger.pos_tag(self.texts)
        tree = parser.parse(sentence_tagged)
        return tree
