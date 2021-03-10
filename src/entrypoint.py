"""
call functions in here
"""
from typing import Text
from src.Language import Language, IPAtoIPA

def create_conlang() -> Language:
    pass

def load_conlang(filename: Text) -> Language:
    pass

def tryout():
    from eng_to_ipa import convert as toIPA
    teststr = "testing this code out!"
    print(toIPA(teststr))

    converter = IPAtoIPA()
    print(converter.convert(toIPA(teststr)))

tryout()