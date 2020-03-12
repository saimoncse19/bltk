from bltk.langtools.taggertools import adjective_suffix, noun_suffix, verb_suffix, pronouns
from bltk.langtools.pos_tagger import PosTagger


class UgraStemmer:
    def __init__(self):
        self.pos_tagger = PosTagger()
        self.pronoun_values = list(pronouns.values())
        self.pronoun_keys = list(pronouns.keys())

    def get_tag(self, sentence: list):
        tagged_sentence = self.pos_tagger.pos_tag(sentence)
        return tagged_sentence

    def stem(self, sentence: list):

        stemmed = []

        if len(sentence) == 0:
            return None

        elif len(sentence) > 0:
            tagged_sentence = self.get_tag(sentence)
            for word, tag in tagged_sentence:
                if (str(word).endswith('ও') or str(word).endswith('ই')) and len(word) > 2:
                    word = word.replace(word[-1], "")
                if tag in ["JJ", "JQ"]:
                    flag = False
                    for suf in adjective_suffix:
                        if str(word).endswith(suf) and (len(word) - len(suf) >= 2):
                            my_stem = str(word).replace(word[-len(suf):], '')
                            stemmed.append(my_stem)
                            flag = True
                            break
                    if not flag:
                        my_stem = word
                        stemmed.append(my_stem)

                elif tag in ["NC", "NP", "NV", "NST"]:
                    flag = False
                    for suf in noun_suffix:
                        if str(word).endswith(suf) and (len(word) - len(suf) >= 2):
                            my_stem = str(word).replace(word[-len(suf):], '')
                            stemmed.append(my_stem)
                            flag = True
                            break
                    if not flag:
                        my_stem = word
                        stemmed.append(my_stem)

                elif tag in ["VA", "VM"]:
                    flag = False
                    for suf in verb_suffix:
                        if str(word).endswith(suf) and (len(word) - len(suf) >= 2):
                            my_stem = str(word).replace(word[-len(suf):], '')
                            stemmed.append(my_stem)
                            flag = True
                            break
                    if not flag:
                        my_stem = word
                        stemmed.append(my_stem)

                elif tag in ["PPR", "PRF", "PRC", "PRL", "PWH"]:
                    flag = False
                    for pronoun in self.pronoun_values:
                        if word in pronoun:
                            my_stem = self.pronoun_keys[self.pronoun_values.index(pronoun)]
                            stemmed.append(my_stem)
                            flag = True
                            break
                    if not flag:
                        my_stem = word
                        stemmed.append(my_stem)

                else:
                    my_stem = word
                    stemmed.append(my_stem)

            return stemmed


