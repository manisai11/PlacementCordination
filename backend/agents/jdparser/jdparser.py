import spacy
from sklearn.feature_extraction.text import TfidfVectorizer

nlp = spacy.load("en_core_web_sm")
jd = open('jod_description.txt').read()
doc = nlp(jd)

# Named entity extraction
entities = [(ent.text, ent.label_) for ent in doc.ents]

# Skill extraction using TF-IDF
vectorizer = TfidfVectorizer(max_features=20, stop_words='english')
keywords = vectorizer.fit_transform([jd])
print(entities)
print(vectorizer.get_feature_names_out())
