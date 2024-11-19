import re

text = "@John: Šis ir lielisks produkts!!! Vai ne? 👏👏👏 http://example.com"
cleaned_text = re.sub(r'http\S+|[@#]\w+|[^\w\s]|[\U00010000-\U0010ffff]', '', text)
cleaned_text = cleaned_text.lower()
normalized_text = re.sub(r'\s+', ' ', cleaned_text).strip()

print(normalized_text)
