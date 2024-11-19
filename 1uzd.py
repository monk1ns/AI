import spacy
from collections import Counter
import re


nlp = spacy.load("xx_ent_wiki_sm") 
text = input("Ievadi tekstu:  ")
text_cleaned = re.sub(r'[^\w\s]', '', text.lower())
doc = nlp(text_cleaned)
word_frequency = Counter([token.text for token in doc if token.is_alpha])

for word, freq in word_frequency.items():
    print(f"'{word}' | Biežums: {freq}")
