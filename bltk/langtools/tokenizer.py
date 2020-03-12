"""
#///////////////////////////////////
    Author: Saimon
    Email: saimoncse19@gmail.com
    Dated: April 12, 2019
#//////////////////////////////////
"""


from bltk.langtools.banglachars import punctuations


class Tokenizer:

    def __init__(self):
        self.punctuations = set(punctuations).difference({"-"})

    @staticmethod
    def sentence_tokenizer(text: str) -> list:

        terminator = ["।", "?", "!"]
        tokens = []
        for i in text:
            if i in terminator:
                my_string = text[:text.index(i)+1]
                text = text[text.index(i)+1:]
                tokens.append(my_string.strip())
        return tokens

    def word_tokenizer(self, text: str):
        tokens = [i for i in text.split()]
        final_tokens = []

        for i in tokens:
            word = i.strip()
            if word[-1] in self.punctuations:
                a = word[:-1]
                b = word[-1]
                final_tokens.append(a)
                final_tokens.append(b)
            elif word[0] in self.punctuations:
                a = word[1:]
                b = word[0]
                final_tokens.append(a)
                final_tokens.append(b)
            else:
                final_tokens.append(word)

        return final_tokens

    def sentence_splitter(self, sentences: list):
        tokens = []
        for sentence in sentences:
            tokens.append(self.word_tokenizer(sentence))

        return tokens
