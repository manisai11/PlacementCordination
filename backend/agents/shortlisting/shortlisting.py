import pandas as pd
df = pd.DataFrame([{"Name": "A", "Similarity": 0.82},
                   {"Name": "B", "Similarity": 0.65}])
shortlisted = df[df['Similarity'] >= 0.75]
print("Shortlisted Students:\n", shortlisted)
