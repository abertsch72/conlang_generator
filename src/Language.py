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

class IPAtoLetters:
    def __init__(self):
        from src.IPA_symbols import VOWELS, CONSONANTS
        from random import randint
        self.letterMap = {}

        num_consonants = len(CONSONANTS.CONSONANT_LETTERS)
        for char in CONSONANTS.ALL_PULMONIC:
            self.letterMap[char] = CONSONANTS.CONSONANT_LETTERS[randint(0, num_consonants - 1)]

        num_vowels = len(VOWELS.VOWEL_LETTERS)
        for char in VOWELS.ALL_VOWELS:
            self.letterMap[char] = VOWELS.VOWEL_LETTERS[randint(0, num_vowels - 1)]

    def convert(self, sentence: Text) -> Text:
        from string import whitespace
        out = ""
        for symbol in sentence:
            if symbol in self.letterMap.keys():
                out += self.letterMap[symbol]
            elif symbol in whitespace:
                out += symbol
            else:
                print(symbol)
        return out


class SyntaxRules:
    def __init__(self):
        pass

    def convert(self, sentence) -> Text:
        pass