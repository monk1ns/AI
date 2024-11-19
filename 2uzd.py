from langdetect import detect

text = input("Ievadiet tekstu: ")
language = detect(text)
print(f"'{text}' | Valoda: {language}")
