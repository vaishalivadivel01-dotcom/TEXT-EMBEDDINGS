<<<<<<< HEAD
# TEXT-EMBEDDINGS
=======
# Text Embeddings using Sentence Transformers

## Objective

The objective of this project is to understand text embeddings and their role
in Large Language Models. Sentence embeddings are generated using a pretrained
Sentence Transformer model and cosine similarity is used to compare sentence
pairs.

## Model Used

- Model: all-MiniLM-L6-v2
- Library: Sentence Transformers

## Dataset

The project uses 20 sentences stored in:

`dataset/generated_text.csv`

## Methodology

1. Load the sentence dataset.
2. Load the `all-MiniLM-L6-v2` Sentence Transformer model.
3. Generate embeddings for the sentences.
4. Display the embedding dimensions.
5. Create sentence pairs.
6. Calculate cosine similarity scores.
7. Identify the top five most similar sentence pairs.
8. Display the similarity matrix.
9. Compare similar and unrelated sentence pairs.
10. Save the generated embeddings and similarity results.

## Output Files

- `embeddings.npy` – stores the sentence embeddings.
- `sentence_pairs.csv` – stores the selected sentence pairs and their scores.
- `similarity_scores.csv` – stores cosine similarity scores.
- `Week4_Text_Embeddings.ipynb` – contains the notebook analysis.

## Importance of Text Embeddings

Text embeddings represent sentences as numerical vectors. Sentences with
related meanings can have similar vector representations. These embeddings
are useful for semantic search and can support applications such as
Retrieval-Augmented Generation (RAG).

## Conclusion

Text embeddings help computers represent and compare the meaning of text.
Using Sentence Transformers and cosine similarity, we can measure semantic
similarity between sentences and prepare vector representations for
semantic-search applications.
>>>>>>> 2d5df42 (Add text embeddings project)
