import re


text1 = "Rudens lapas ir dzeltenas un oranžas. Lapas klāj zemi un padara to krāsainu."
text2 = "Krāsainas rudens lapas krīt zemē. Lapas ir oranžas un dzeltenas."
def clean_and_tokenize(text):
    text_cleaned = re.sub(r'[^\w\s]', '', text.lower())  
    words = text_cleaned.split()  
    return set(words)  

words_text1 = clean_and_tokenize(text1)
words_text2 = clean_and_tokenize(text2)
common_words = words_text1.intersection(words_text2)
common_count = len(common_words)
total_words = len(words_text1.union(words_text2))  
similarity_percentage = (common_count / total_words) * 100
print(f"Kopīgie vārdi: {common_words}")
print(f"Sakritības līmenis: {similarity_percentage:.2f}%")
