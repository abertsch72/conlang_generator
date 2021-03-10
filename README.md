# conlang_generator
Playing around with conlang generation using syntax trees and IPA


## Step 1: Different letters
- [x] Convert from English -> IPA
- [x] Direct substitution by IPA character-- e.g. /tɛstɪŋ/ into /ʔɑsʔəɡ/
- [x] Conversion from IPA -> shuffled letters
- [ ] Restore punctuation
- [ ] Save and load in a previous language!

## Step 2: Different number of letters
- [ ] Bigram IPA character substitution
- [ ] Bigram into unigram/bigram/trigram substitution (changes up number of letters in the word)

## Step 3: Different order
- [ ] Get and parse syntax trees
- [ ] Produce list of linguistic "switches" -- e.g. word order
- [ ] Shuffle switches and apply to sentence

## Step 4: Different number of words
- [ ] Add word-combining/word-adding "switches" to the list
- [ ] Apply these to sentences

## Step 5: Make this less English-centric and more robust
- [ ] Add non-English letters
- [ ] Add translation to English before conversion -- probably more robust than trying to find IPA converters for every language
- [ ] Add some support for words not in the CMU IPA dictionary

## Step 6: Make this reasonable to learn 
- [ ] Some kind of checks for ease of pronunciation? Not sure what this entails tbh
