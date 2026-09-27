from sentence_transformers import SentenceTransformer
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


# 1. Load the dataset
data = pd.read_csv("dataset/generated_text.csv")

sentences = data["sentence"].tolist()

print("Number of sentences:", len(sentences))


# 2. Load the Sentence Transformer model
model = SentenceTransformer("all-MiniLM-L6-v2")


# 3. Generate embeddings
embeddings = model.encode(sentences)

print("Embedding shape:", embeddings.shape)
print("Embedding dimension:", embeddings.shape[1])


# 4. Save embeddings
np.save("dataset/embeddings.npy", embeddings)

print("Embeddings saved successfully.")


# 5. Create sentence pairs
pairs = [
    (0, 4),
    (0, 19),
    (1, 12),
    (2, 13),
    (3, 0),
    (5, 6),
    (7, 8),
    (10, 11),
    (14, 16),
    (17, 18)
]


# 6. Calculate cosine similarity
results = []

for i, j in pairs:

    score = cosine_similarity(
        [embeddings[i]],
        [embeddings[j]]
    )[0][0]

    results.append({
        "sentence_1": sentences[i],
        "sentence_2": sentences[j],
        "similarity_score": score
    })


# 7. Create DataFrame
similarity_df = pd.DataFrame(results)


# 8. Save sentence pairs
similarity_df.to_csv(
    "dataset/sentence_pairs.csv",
    index=False
)


# 9. Save similarity scores
similarity_df.to_csv(
    "dataset/similarity_scores.csv",
    index=False
)


# 10. Display results
print("\nSentence Pair Similarity Scores:")
print(similarity_df)


# 11. Display top 5 similar pairs
top_5 = similarity_df.sort_values(
    by="similarity_score",
    ascending=False
).head(5)

print("\nTop 5 Most Similar Sentence Pairs:")
print(top_5)