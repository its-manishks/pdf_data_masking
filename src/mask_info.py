import re
import spacy

# Load a pre-trained model for Named Entity Recognition (NER)
nlp = spacy.load("en_core_web_sm")

def mask_sensitive_info(text):
    sensitive_words = []
    
    # Mask names using NER
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            sensitive_words.append(ent.text)
    
    # Mask phone numbers
    sensitive_words.extend(re.findall(r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b', text))
    
    # Mask email addresses
    sensitive_words.extend(re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text))

    return sensitive_words
