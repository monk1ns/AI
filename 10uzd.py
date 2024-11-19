from googletrans import Translator

translator = Translator()

latvian_texts = [
    "Labdien! Kā jums klājas?",
    "Es šodien lasīju interesantu grāmatu."
]

def translate_to_english(texts):
    translated_texts = []
    for text in texts:
        translated = translator.translate(text, src='lv', dest='en')
        translated_texts.append(translated.text)
    return translated_texts
translated_texts = translate_to_english(latvian_texts)
for lt, en in zip(latvian_texts, translated_texts):
    print(f"Latviski: {lt}")
    print(f"Angliski: {en}")
    print()
