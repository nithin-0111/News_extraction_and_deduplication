import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os
import numpy as np

def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

def remove_duplicates(df, threshold=0.9):
    combined_text = df['article'] + " " + df['highlights']
    vectorizer = TfidfVectorizer(max_features=5000)
    tfidf_matrix = vectorizer.fit_transform(combined_text)
    similarity_matrix = cosine_similarity(tfidf_matrix)
    np.fill_diagonal(similarity_matrix, 0)

    duplicates = set()
    for i in range(len(df)):
        for j in range(i + 1, len(df)):
            if similarity_matrix[i, j] > threshold:
                duplicates.add(j)

    print(f"Found {len(duplicates)} duplicates.")
    return list(duplicates)

def main():
    file_path = "D:/Newspaper_Deduplication/newspaper_articles.csv"
    print(f"Looking for file at: {os.path.abspath(file_path)}")

    if os.path.exists(file_path):
        print("File exists!")
    else:
        print("File not found!")
        return

    print("Loading data...")
    df = load_data(file_path)
    print("Removing duplicates...")
    duplicate_indices = remove_duplicates(df)
    unique_df = df.drop(duplicate_indices)
    unique_df.to_csv("deduplicated_articles.csv", index=False)
    print("Deduplication complete. Results saved to 'deduplicated_articles.csv'.")

if __name__ == "__main__":
    main()
