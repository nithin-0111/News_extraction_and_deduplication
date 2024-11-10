# Deduplication Script

## Overview

This script is made to read a CSV file that has articles and highlights, find duplicate entries based on how similar they are, and save a cleaned-up version of the data to a new CSV file. It uses TF-IDF (Term Frequency-Inverse Document Frequency) and cosine similarity to help find and remove duplicate articles.

## How the Code Works

### 1. Loading the Data
First, the code loads a CSV file from the given path. This file is supposed to have two columns: **article** and **highlights**. These two columns are combined into one string so that both the article content and the highlights affect the similarity check equally.

### 2. TF-IDF Vectorization
To measure text similarity, the script uses a **TF-IDF Vectorizer** to change text data into a numeric format that can be compared with math. The vectorizer limits the vocabulary to 5000 words to keep things fast and reduce memory usage. The `fit_transform` function does two things at once: it learns the vocabulary from the text and produces a matrix representing each article with a vector of TF-IDF values.

### 3. Calculating Cosine Similarity
Next, it calculates the **cosine similarity** between the articles. This basically tells us how close each article is to the others. Then, the code sets the diagonal of this similarity matrix to zero, so an article doesn’t compare itself, which would always show a perfect match.

### 4. Identifying Duplicates
The code uses a set to hold the indices of the duplicates it finds. It compares pairs of articles and considers them duplicates if their similarity score is above a certain threshold (0.9 by default). It then converts the set to a list and returns it, so we have a list of duplicate entries.

### 5. Main Function
The main function checks if the file exists at the specified path. If the file is there, it loads the data, runs the duplicate check, and drops duplicates from the DataFrame. Finally, it saves the cleaned data to a new file called **deduplicated_articles.csv**.

### 6. Running the Code
To run the script, just execute it in your Python environment. It will go through all steps automatically and save the deduplicated results for you.

For the current data, the model identified 76 duplicates, and generated a new deduplicated_articles.csv after removing the duplicates.

# Requirements

* transformers
* scikit-learn
* pandas
* numpy
