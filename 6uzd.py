import spacy

try:
    nlp = spacy.load("lv_core_news_lg")  
except OSError:
    nlp = spacy.blank("lv")
if "parser" not in nlp.pipe_names:
    sentencizer = nlp.add_pipe("sentencizer")

article = """
Latvija ir valsts Baltijas reģionā. Tās galvaspilsēta ir Rīga, kas ir slavena ar savu vēsturisko centru un skaistajām ēkām. 
Latvija robežojas ar Lietuvu, Igauniju un Krieviju, kā arī tai ir piekļuve Baltijas jūrai. Tā ir viena no Eiropas Savienības dalībvalstīm.
"""
doc = nlp(article)
sentences = list(doc.sents)
important_sentences = sentences[:2]
summary = " ".join([sent.text for sent in important_sentences])

print("Rezumējums:")
print(summary)
