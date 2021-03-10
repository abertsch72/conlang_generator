from typing import Text


class Language:
    def __init__(self):
        rules = None
        IPA_map = None

    def convert(self, sentence: Text) -> Text:
        pass


class IPAtoIPA:
    def __init__(self):
        from src.IPA_symbols import CONSONANTS, VOWELS
        from random import shuffle

        shuffledC = CONSONANTS.ALL_PULMONIC.copy()
        shuffle(shuffledC)

        shuffledV = VOWELS.ALL_VOWELS.copy()
        shuffle(shuffledV)

        self.IPAmap = dict(zip(CONSONANTS.ALL_PULMONIC + VOWELS.ALL_VOWELS, shuffledC + shuffledV))

    def convert(self, sentence: Text) -> Text:
        from string import whitespace
        out = ""
        for symbol in sentence:
            if symbol in self.IPAmap.keys():
                out += self.IPAmap[symbol]
            elif symbol in whitespace:
                out += symbol
            else:
                print(symbol)
        return out

class IPAtoLatin:
    def __init__(self):
        map = {}

    def convert(self, sentence: Text) -> Text:
        pass


class SyntaxRules:
    def __init__(self):
        pass

    def convert(self, sentence) -> Text:
        pass