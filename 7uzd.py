import spacy

# Ielādēsim lielo angļu valodas modeli
nlp = spacy.load("en_core_web_md")

# Vārdi, kurus analizēt
words = ["house", "apartment", "sea"]

# Iegūstam vektorus katram vārdam
vectors = {word: nlp(word).vector for word in words}

# Funkcija, kas aprēķina semantisko līdzību starp diviem vārdiem
def similarity(word1, word2):
    return nlp(word1).similarity(nlp(word2))

# Salīdzinām līdzības
similarities = {}
for i, word1 in enumerate(words):
    for word2 in words[i+1:]:
        sim_score = similarity(word1, word2)
        similarities[(word1, word2)] = sim_score

# Izdrukāsim iegūtos vektorus un līdzības
print("Vektori:")
for word, vec in vectors.items():
    print(f"{word}: {vec[:5]}...")  # Izdodam tikai pirmos 5 elementus, jo vektori ir garš

print("\nSemantiskā līdzība starp vārdiem:")
for (word1, word2), score in similarities.items():
    print(f"Līdzība starp '{word1}' un '{word2}': {score:.4f}")
