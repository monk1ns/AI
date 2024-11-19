import spacy
import re

nlp = spacy.load("xx_ent_wiki_sm")

text = "Valsts prezidents Egils Levits piedalījās pasākumā, ko organizēja Latvijas Universitāte."

doc = nlp(text)

def identify_organization(ent):
    if isinstance(ent, spacy.tokens.Span):
        organization_keywords = ["Universitāte", "Skola", "Institūts"]
        if any(keyword in ent.text for keyword in organization_keywords):
            return "ORG"
    return ent.label_

for ent in doc.ents:
    entity_type = identify_organization(ent)
    print(f"Teksts: {ent.text}, Tips: {entity_type}")
