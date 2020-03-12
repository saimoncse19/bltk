
# BLTK: The Bengali Natural Language Processing Toolkit

A lightweight but robust toolkit for processing Bengali Language.

[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=102)](https://github.com/ellerbrock/open-source-badge/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)


## Overview
BLTK is a lightweight but exceptionally robust language processing toolkit for the Bengali Language. I, Mr. Saimon Hossain, along with my friend, Mr. Liton Shil, have conducted research as a part of our undergraduate thesis under the supervision of our respected sir, Mr. Sowmitra Das. This is the outcome of our 6 month long research & development project. 

I have choosen this name after taking inspiration from the popular natural language processing toolkit - **NLTK**.

BLTK is still in its childhood. It's maturing everyday. It'll receive updates in the days to come. 

If you want to contribute to BLTK's growth, please read the contribution section at the end of this page. 

## Supported Functionalities
- Word Tokenization
- Sentence Tokenization
- Sentence Splitting
- Stopwords Filtering
- Statistical Part-of-speech Tagging
- Phrase Chunking/Named-Entity Recognition
- Stemming



## Installation
To get BLTK up and running, run the following command.
```sh
pip install bltk
```

## Usage

### 1) The Bengali Characters
In **BLTK**, the ***banglachars*** module contains 7 lists of characters specific to the Bengali Language.
1. vowels
2. vowel signs
3. consonants
4. digits
5. punctuation marks
6. operators
7. others

#### Code
```python
from bltk.langtools.banglachars import (vowels,
                                        vowel_signs,
                                        consonants,
                                        digits,
                                        operators,
                                        punctuations,
                                        others)
print(f'Vowels: {vowels}')
print(f'Vowel signs: {vowel_signs}')
print(f'Consonants: {consonants}')
print(f'Digits: {digits}')
print(f'Operators: {operators}')
print(f'Punctuation marks: {punctuations}')
print(f'Others: {others}')
```

#### Output
```
Vowels: ['অ', 'আ', 'ই', 'ঈ', 'উ', 'ঊ', 'ঋ', 'ঌ', 'এ', 'ঐ', 'ও', 'ঔ']
Vowel signs: ['া', 'ি', 'ী', 'ু', 'ূ', 'ৃ', 'ৄ', 'ে', 'ৈ', 'ো', 'ৌ']
Consonants: ['ক', 'খ', 'গ', 'ঘ', 'ঙ', 'চ', 'ছ', 'জ', 'ঝ', 'ঞ', 'ট', 'ঠ', 'ড', 'ঢ', 'ণ', 'ত', 'থ', 'দ', 'ধ', 'ন', 'প', 'ফ', 'ব', 'ভ', 'ম', 'য', 'র', 'ল', 'শ', 'ষ', 'স', 'হ', 'ড়', 'ঢ়', 'য়', 'ৎ', 'ং', 'ঃ', 'ঁ']
Digits: ['০', '১', '২', '৩', '৪', '৫', '৬', '৭', '৮', '৯']
Operators: ['=', '+', '-', '*', '/', '%', '<', '>', '×', '÷']
Punctuation marks: ['।', ',', ';', ':', '?', '!', "'", '.', '"', '-', '[', ']', '{', '}', '(', ')', '–', '—', '―', '~']
Others: ['৳', '৺', '্', 'ঀ', 'ঽ', '#', '$']

```



### 2) Word Tokenization
In **BLTK**, the ***word_tokenizer(text: str)*** method of the Tokenizer class performs word tokenization. It takes a text string and returns a list of tokenized words. The Following code shows how it is done.

#### Code
```python
from bltk.langtools import Tokenizer

# Sample text
text = "আমি জানি আমার এই লেখাটির জন্য আমাকে অনেক গালমন্দ শুনতে হবে, তারপরেও লিখছি। "\
       "লিখে খুব কাজ হয় সে রকম উদাহরণ আমার হাতে খুব বেশী নেই কিন্তু অন্তত নিজের ভেতরের ক্ষোভটুকু বের করা " \
       "যায় সেটাই আমার জন্যে অনেক।"

# Creating an instance
tokenizer = Tokenizer()

# Tokenizing words
print('TOKENIZED WORDS')
words = tokenizer.word_tokenizer(text)
print(words)
```

#### Output
```
TOKENIZED WORDS
['আমি', 'জানি', 'আমার', 'এই', 'লেখাটির', 'জন্য', 'আমাকে', 'অনেক', 'গালমন্দ', 'শুনতে', 'হবে', ',', 'তারপরেও', 'লিখছি', '।', 'লিখে', 'খুব', 'কাজ', 'হয়', 'সে', 'রকম', 'উদাহরণ', 'আমার', 'হাতে', 'খুব', 'বেশী', 'নেই', 'কিন্তু', 'অন্তত', 'নিজের', 'ভেতরের', 'ক্ষোভটুকু', 'বের', 'করা', 'যায়', 'সেটাই', 'আমার', 'জন্যে', 'অনেক', '।']

```

### 3) Sentence Tokenization
In Bengali, most of the sentence delimiters are same as in English except full-stop. Statements and imperative sentences are terminated by । - the Devanagari Danda.
Questions and exclamatory sentences are terminated by ? and ! respectively. 

In **BLTK**, the ***sentence_tokenizer(text: str)*** method of the Tokenizer class performs sentence tokenization. It takes a text string and returns a list of tokenized sentences. The Following code shows how it is done.

#### Code
```python
from bltk.langtools import Tokenizer

# Sample text
text = "আমি জানি আমার এই লেখাটির জন্য আমাকে অনেক গালমন্দ শুনতে হবে, তারপরেও লিখছি। " \
       "লিখে খুব কাজ হয় সে রকম উদাহরণ আমার হাতে খুব বেশী নেই কিন্তু অন্তত নিজের ভেতরের ক্ষোভটুকু বের করা " \
       "যায় সেটাই আমার জন্যে অনেক।"

# Creating an instance
tokenizer = Tokenizer()


# Tokenizing Sentences
print("TOKENIZED SENTENCES")
sentences = tokenizer.sentence_tokenizer(text)
print(sentences)
```

#### Output
```
TOKENIZED SENTENCES
['আমি জানি আমার এই লেখাটির জন্য আমাকে অনেক গালমন্দ শুনতে হবে, তারপরেও লিখছি।', 'লিখে খুব কাজ হয় সে রকম উদাহরণ আমার হাতে খুব বেশী নেই কিন্তু অন্তত নিজের ভেতরের ক্ষোভটুকু বের করা যায় সেটাই আমার জন্যে অনেক।']
```



### 4) Sentence Split
The ***sentence_splitter(sentence: list)*** method takes a list of tokened sentences and then splits them into their corresponding list of tokened words with the help of word_tokenizer() method. The return value is a list of tokened words lists.

#### Code
```python
from bltk.langtools import Tokenizer

# Sample text
text = "আমি জানি আমার এই লেখাটির জন্য আমাকে অনেক গালমন্দ শুনতে হবে, তারপরেও লিখছি। " \
       "লিখে খুব কাজ হয় সে রকম উদাহরণ আমার হাতে খুব বেশী নেই কিন্তু অন্তত নিজের ভেতরের ক্ষোভটুকু বের করা " \
       "যায় সেটাই আমার জন্যে অনেক।"

# Creating an instance
tokenizer = Tokenizer()


# Tokenizing Sentences
sentences = tokenizer.sentence_tokenizer(text)

print("SPLIT SENTENCES")
sentence_list = tokenizer.sentence_splitter(sentences)
print(sentence_list)

print("INDIVIDUAL SENTENCE")
for i in sentence_list:
    print(i)

```

#### Output
```
SPLIT SENTENCES
[['আমি', 'জানি', 'আমার', 'এই', 'লেখাটির', 'জন্য', 'আমাকে', 'অনেক', 'গালমন্দ', 'শুনতে', 'হবে', ',', 'তারপরেও', 'লিখছি', '।'], ['লিখে', 'খুব', 'কাজ', 'হয়', 'সে', 'রকম', 'উদাহরণ', 'আমার', 'হাতে', 'খুব', 'বেশী', 'নেই', 'কিন্তু', 'অন্তত', 'নিজের', 'ভেতরের', 'ক্ষোভটুকু', 'বের', 'করা', 'যায়', 'সেটাই', 'আমার', 'জন্যে', 'অনেক', '।']]

INDIVIDUAL SENTENCE

['আমি', 'জানি', 'আমার', 'এই', 'লেখাটির', 'জন্য', 'আমাকে', 'অনেক', 'গালমন্দ', 'শুনতে', 'হবে', ',', 'তারপরেও', 'লিখছি', '।']
['লিখে', 'খুব', 'কাজ', 'হয়', 'সে', 'রকম', 'উদাহরণ', 'আমার', 'হাতে', 'খুব', 'বেশী', 'নেই', 'কিন্তু', 'অন্তত', 'নিজের', 'ভেতরের', 'ক্ষোভটুকু', 'বের', 'করা', 'যায়', 'সেটাই', 'আমার', 'জন্যে', 'অনেক', '।']


```


### 5) Stopwords Filtering
**BLTK's** ***remove_stopwords(words: list, *,  level: str = "soft")*** function by default performs a soft stopwords elimination. It takes two parameters: **a list of words** and a **keyword argument** which can be either 'soft', 'moderate' or 'hard'. If no parameter is given, a soft elimination is performed.

Filtering stopwords is not always an ideal choice. In any language, there is no universal list of stop words, and sometimes different researchers use different methods for eliminating stopwords. If you are not sure about which level to use, use the default.


#### Code
```python
from bltk.langtools import remove_stopwords
from bltk.langtools import Tokenizer

tokenizer = Tokenizer()

text = "আমি জানি আমার এই লেখাটির জন্য আমাকে অনেক গালমন্দ শুনতে হবে, তারপরেও লিখছি। " \
       "লিখে খুব কাজ হয় সে রকম উদাহরণ আমার হাতে খুব বেশী নেই কিন্তু অন্তত নিজের ভেতরের ক্ষোভটুকু বের করা " \
       "যায় সেটাই আমার জন্যে অনেক।"

tokened_words = tokenizer.word_tokenizer(text)

print(f"Len of words: {len(tokened_words)}")
print(f"After soft elimination: {(remove_stopwords(tokened_words))}")
print(f"Length after soft elimination: {len(remove_stopwords(tokened_words))}")
print(f"After moderate elimination: {(remove_stopwords(tokened_words, level='moderate'))}")
print(f"Length after moderate elimination: {len(remove_stopwords(tokened_words, level='moderate'))}")
print(f"After hard elimination: {(remove_stopwords(tokened_words, level='hard'))}")
print(f"Length after hard elimination: {len(remove_stopwords(tokened_words, level='hard'))}")

```

#### Output
```
Len of words: 40
After soft elimination: ['জানি', 'লেখাটির', 'অনেক', 'গালমন্দ', 'শুনতে', 'তারপরেও', 'লিখছি', 'লিখে', 'কাজ', 'রকম', 'উদাহরণ', 'হাতে', 'বেশী', 'অন্তত', 'ভেতরের', 'ক্ষোভটুকু', 'বের', 'করা', 'সেটাই', 'অনেক']
Length after soft elimination: 20
After moderate elimination: ['জানি', 'লেখাটির', 'গালমন্দ', 'শুনতে', 'তারপরেও', 'লিখছি', 'লিখে', 'উদাহরণ', 'হাতে', 'বেশী', 'ভেতরের', 'ক্ষোভটুকু', 'বের', 'যায়', 'জন্যে']
Length after moderate elimination: 15
After hard elimination: ['জানি', 'লেখাটির', 'গালমন্দ', 'শুনতে', 'তারপরেও', 'লিখছি', 'লিখে', 'উদাহরণ', 'হাতে', 'বেশী', 'ভেতরের', 'ক্ষোভটুকু', 'বের']
Length after hard elimination: 13

```


### 6) Statistical Part-of-speech Tagging
**BLTK** includes a statistical POS tagger which has an overall system accuracy of 95.9%.
The POS tagger works in sentence-level which means that instead of tagging a word individually, it tags words in a sentence or a phrase, taking features such as ***previous word*** and ***next word*** into consideration. It relies on the Logistic Regression classifier. 

The BLTK's PosTagger class has a method ***pos_tag()*** which takes a list of split sentences and returns a list of tagged sentences. 
Each tagged sentence is a list of ***tuples of length 2*** each, where the first index of the tuple holds the word itself and the last index holds its corresponding tag.


#### Code
```python
from bltk.langtools import PosTagger
from bltk.langtools import Tokenizer

pos_tagger = PosTagger()
tokenizer = Tokenizer()

text = "আমি জানি আমার এই লেখাটির জন্য আমাকে অনেক গালমন্দ শুনতে হবে, তারপরেও লিখছি। " \
       "লিখে খুব কাজ হয় সে রকম উদাহরণ আমার হাতে খুব বেশী নেই কিন্তু অন্তত নিজের ভেতরের ক্ষোভটুকু বের করা " \
       "যায় সেটাই আমার জন্যে অনেক।"

token_text = tokenizer.sentence_tokenizer(text)


pos_tags = []
for text in token_text:
    tokened = tokenizer.word_tokenizer(text)
    tagged = pos_tagger.pos_tag(tokened)
    pos_tags.append(tagged)
print(pos_tags)
```

#### Output
```
[[('আমি', 'PPR'), ('জানি', 'VM'), ('আমার', 'PPR'), ('এই', 'DAB'), ('লেখাটির', 'NC'), ('জন্য', 'PP'), ('আমাকে', 'PPR'), ('অনেক', 'JQ'), ('গালমন্দ', 'NC'), ('শুনতে', 'VM'), ('হবে', 'VA'), (',', 'PU'), ('তারপরেও', 'ALC'), ('লিখছি', 'VM'), ('।', 'PU')], [('লিখে', 'VM'), ('খুব', 'JQ'), ('কাজ', 'NC'), ('হয়', 'VM'), ('সে', 'PPR'), ('রকম', 'NC'), ('উদাহরণ', 'NC'), ('আমার', 'PPR'), ('হাতে', 'NC'), ('খুব', 'JQ'), ('বেশী', 'JJ'), ('নেই', 'VM'), ('কিন্তু', 'CSB'), ('অন্তত', 'CSB'), ('নিজের', 'PRF'), ('ভেতরের', 'NST'), ('ক্ষোভটুকু', 'NC'), ('বের', 'VM'), ('করা', 'NV'), ('যায়', 'VM'), ('সেটাই', 'PPR'), ('আমার', 'PPR'), ('জন্যে', 'PP'), ('অনেক', 'JQ'), ('।', 'PU')]]


```



### 7) Phrase Chunking/Named-Entity Recognition
**BLTK's** phrase chunker can find out all the phrases in a given text as long as a correct grammatical syntax for that phrase is provided in the form of a regular expression. The performance of the chunker is unparalleled since it heavily relies on the BLTK's POS Tagger which has an outstanding accuracy and NLTK's Regular Expression Parser which is extremely powerful. 

BLTK's Chunker class has method named ***chunk()*** that takes two parameters: ***a grammar*** in the form of regular expression, and ***a text*** from which phrases will be extracted.

This section explains how to create a noun phrase chunker using BLTK's Chunker class and a regular expression grammar. A noun phrase begins with an optional demonstrative, followed by zero or more adjectives/quantifiers and terminates with a noun.
Some examples of Bangla noun phrases are given below:

NP: (NP গণতন্ত্র/NC) - a noun phrase with only one noun.
    
NP: (NP মানবিক/JJ বোধ/NC) - a noun phrase with an adjective followed by a noun.
    
NP: (NP এই/DAB সুন্দর/JJ লেখাটির/NC) - a noun phrase with a demonstrative, followed by an adjective and terminated by a noun.


The grammar for extracting Bangla noun phrases can be constructed with the following regular expression.

```
 NP: {<DAB|DRL>?<JJ|JQ>*<N.>} 
```
The tags used to construct the grammar as well as training the POS Tagger have been explained in the following table as specified by reserachers at **Microsof Research, India**. Grammars for verb phrases, named entities, etc. can also be constructed in the similar fashion. 

| Name                   | Tag     | Example    |
|------------------------|---------|------------|
| COMMON NOUN            | NC      |  মানুষ      |
| PROPER NOUN            | NP      | রবীন্দ্রনাথ  |
| VERBAL NOUN            | NV      | ঘটানো      |
| SPATIO-TEMPORAL NOUN   | NST     | উপরে       |
| MAIN VERB              | VM      | করছিলেন    |
| AUXILIARY VERB         | VA      | এসে        |
| PRONOMINAL PRONOUN     | PPR     | আমাদের     |
| REFLEXIVE PRONOUN      | PRF     | নিজ        |
| RECIPROCAL PRONOUN     | PRC     | পরস্পর      |
| RELATIVE PRONOUN       | PRL     | যাহার      |
| WH-PRONOUN             | PWH     | কেন        |
| ADJECTIVE              | JJ      | গুরুত্বপূর্ণ    |
| QUANTIFIER             | JQ      | কয়েকটি     |
| ABSOLUTE DEMONSTRATIVE | DAB     | এই         |
| RELATIVE DEMONSTRATIVE | DRL     | যে         |
| WH-DEMONSTRATIVE       | DWH     | কী         |
| ADVERB of MANNER       | AMN     | আবার       |
| ADVERB of LOCATION     | ALC     | যখন        |
| CONDITIONAL PARTICIPLE | LC      | হলেই       |
| VERBAL PARTICIPLE      | LV      | বইতে-বইতেই |
| POSTPOSITION           | PP      | জন্য        |
| COORDINATING PARTICLE  | CCD     | এবং        |
| SUBORDINATING PARTICLE | CSB     | সুতরাং      |
| CLASSIFIER PARTICLE    | CCL     | প্রমুখ       |
| INTERJECTION           | CIN     | আরে        |
| OTHER PARTICLE         | CX      | তাই        |
| PUNCTUATION            | PU      | ৷          |
| FOREIGN WORD           | RDF     | Schedule   |
| SYMBOL                 | RDS     | \$         |
| OTHER                  | RDX     | ৩৫৬        |



Like grammar for noun phrases, grammar for verb phrases, postpositional phrases, etc. can be constructed with valid regular expressions.

#### Code
```python
from bltk.langtools import Tokenizer
from bltk.langtools import Chunker


grammar = r"""
  NP: {<DAB>?<JJ|JQ>*<N.>}      
  """
text = "আমি জানি আমার এই লেখাটির জন্য আমাকে অনেক গালমন্দ শুনতে হবে, তারপরেও লিখছি। " \
       "লিখে খুব কাজ হয় সে রকম উদাহরণ আমার হাতে খুব বেশী নেই কিন্তু অন্তত নিজের ভেতরের ক্ষোভটুকু বের করা " \
       "যায় সেটাই আমার জন্যে অনেক।"

tokenizer = Tokenizer()
sentences = tokenizer.sentence_tokenizer(text)
tokened_text = [tokenizer.word_tokenizer(sentence) for sentence in sentences]

noun_phrases = []
for t in tokened_text:
    chunky = Chunker(grammar=grammar, tokened_text=t)
    chunk_tree = chunky.chunk()
    for i in chunk_tree.subtrees():
        if i.label() == "NP":
            print(i)
            noun_phrases.append(i)
```

#### Output
```
(NP এই/DAB লেখাটির/NC)
(NP অনেক/JQ গালমন্দ/NC)
(NP খুব/JQ কাজ/NC)
(NP রকম/NC)
(NP উদাহরণ/NC)
(NP হাতে/NC)
(NP ক্ষোভটুকু/NC)
(NP করা/NV)

```

**Note:** BLTK's Phrase Chunker relies on BLTK's POS Tagger and NLTK's RegexParser. For a complete documentation on ***NLTK's Tree class***, which has been used in its RegexParser, follow [this link](https://www.nltk.org/api/nltk.html#nltk.tree.Tree).



### 8) Stemming
BLTK currently supports one stemmer - the **Ugra stemmer**. 
It relies on some pre-arranged lists of suffixes and BLTK's POS Tagger for stemming Bangla words. The reason POS tagging is done before any stemming is even performed is that eliminating suffixes without determining part-of-speech of the words leads to serious miss-stemming issues.

The inflectional morpheme 'ও'  or 'ই' modifies a word such as  'তারপরেও' . Ugra eliminates 'ও' or 'ই' from the end of the words and makes sure that after elimination of it, the lengths of the words are greater than or equal to two in terms of the number of characters.
It should be noted that if 'ও' or 'ই' is an independent word, it's never removed.


#### Code
```python
from bltk.langtools import UgraStemmer
from bltk.langtools import Tokenizer


text = "আমি জানি আমার এই লেখাটির জন্য আমাকে অনেক গালমন্দ শুনতে হবে, তারপরেও লিখছি। " \
       "লিখে খুব কাজ হয় সে রকম উদাহরণ আমার হাতে খুব বেশী নেই কিন্তু অন্তত নিজের ভেতরের ক্ষোভটুকু বের করা " \
       "যায় সেটাই আমার জন্যে অনেক।"

stemmer = UgraStemmer()
tokenizer = Tokenizer()
tokenized_text = tokenizer.word_tokenizer(text)

stem = stemmer.stem(tokenized_text)

print(f"Before stemming: {tokenized_text}")
print(f'After stemming: {stem}')


```

#### Output
```
Before stemming: ['আমি', 'জানি', 'আমার', 'এই', 'লেখাটির', 'জন্য', 'আমাকে', 'অনেক', 'গালমন্দ', 'শুনতে', 'হবে', ',', 'তারপরেও', 'লিখছি', '।', 'লিখে', 'খুব', 'কাজ', 'হয়', 'সে', 'রকম', 'উদাহরণ', 'আমার', 'হাতে', 'খুব', 'বেশী', 'নেই', 'কিন্তু', 'অন্তত', 'নিজের', 'ভেতরের', 'ক্ষোভটুকু', 'বের', 'করা', 'যায়', 'সেটাই', 'আমার', 'জন্যে', 'অনেক', '।']

After stemming: ['আমি', 'জানি', 'আমি', 'এই', 'লেখা', 'জন্য', 'আমি', 'অনেক', 'গালমন্দ', 'শুনতে', 'হবে', ',', 'তারপরে', 'লিখছি', '।', 'লিখে', 'খুব', 'কাজ', 'হয়', 'সে', 'রকম', 'উদাহরণ', 'আমি', 'হাতে', 'খুব', 'বেশ', 'নে', 'কিন্তু', 'অন্তত', 'নিজের', 'ভেতর', 'ক্ষোভ', 'বের', 'করা', 'যায়', 'সেটি', 'আমি', 'জন্যে', 'অনেক', '।']


```

## Contribution
If you want to contribute, please make a pull request and wait for PR confirmation. You can also send me a mail to saimoncse19@gmail.com with the subject **Contributing to BLTK** specifying a little bit about what you are interested to contribute.

Contribution can also be made by adding issues.