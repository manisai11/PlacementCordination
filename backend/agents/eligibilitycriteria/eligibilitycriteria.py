from sentence_transformers import SentenceTransformer, util
model = SentenceTransformer('all-MiniLM-L6-v2')

resume_text = open("resume_text.txt").read()
jd_text = open("job_description.txt").read()

emb1 = model.encode(resume_text, convert_to_tensor=True)
emb2 = model.encode(jd_text, convert_to_tensor=True)
score = util.cos_sim(emb1, emb2)
print(f"Similarity Score: {score.item():.2f}")
