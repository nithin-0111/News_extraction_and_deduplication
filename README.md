# Article Extraction and Deduplication Script

## Overview

This project includes three Python scripts that help you extract articles from URLs, clean up the data, and remove duplicates based on their text similarity. The deduplication is done using two different models: **TF-IDF** and **Sentence-BERT**. The main tasks are:

- **Extracting articles**: Grab the article and title from a list of URLs.
- **Deduplication**: Remove duplicate articles using **TF-IDF** or **Sentence-BERT** based on how similar the text content is.

The result? A cleaned-up CSV file with unique articles that can be used for further analysis or processing.

## Prerequisites

To get started, you'll need to install a few Python libraries:

```bash
pip install newspaper3k sklearn sentence-transformers pandas numpy

```

## File Structure

The project includes the following scripts:

### 1. `extract_articles.py`:

This script takes a list of URLs in .json format, extracts the articles using the `newspaper3k` library, and stores them in a CSV file with a unique ID for each article.

### 2. `tfidf.py`:

This script removes duplicate articles based on their textual similarity using the TF-IDF model. It compares the articles using word frequency vectors and identifies duplicates.

### 3. `sentence_bert.py`:

This script removes duplicates based on the Sentence-BERT model. Sentence-BERT captures the semantic meaning of the sentences, making it more effective at finding paraphrased articles.

## Example JSON Input for Article Extraction:

```json
{
    "urls": [
        "https://example.com/article1",
        "https://example.com/article2",
        "https://example.com/article3"
    ]
}
```

## Example CSV Output After Deduplication:

| id                                    | article                          | highlights                |
|---------------------------------------|----------------------------------|---------------------------|
| 2f3eab25-b0f1-4edb-b436-f184d582569a | Full text of the article goes here. | The Title of the Article  |
| 8b755274-45e2-40c9-8b22-e66f3f607ad2 | Another article's full text here. | Another Article's Title   |

## How the Code Works

### Article Extraction (`extract_articles.py`)

- **Load URLs**: The script starts by reading a JSON file containing a list of URLs.
- **Extract Content**: For each URL, the script uses the `newspaper3k` library to pull out the article's title and content.
- **Generate Unique ID**: Each article gets a unique ID (thanks to `uuid`).
- **Save to CSV**: The article's title, content, and ID are saved to a CSV file.

### Deduplication Process

The deduplication process compares articles to figure out which ones are duplicates. We use two methods for this:

#### 1. TF-IDF Model (`tfidf.py`):

- **How it works**: TF-IDF stands for Term Frequency-Inverse Document Frequency. It’s a fancy way of saying, "Let's figure out which words are important in this article based on their frequency." The script converts the articles into vectors (numbers) based on the words they contain.
- **Cosine Similarity**: After converting the articles to vectors, the script uses cosine similarity to check how similar each article is to others. If two articles are too similar (above a threshold), they’re considered duplicates.
- **Efficiency**: TF-IDF is fast and works well for articles that are very similar in wording, but it doesn’t capture deeper meanings.

#### 2. Sentence-BERT Model (`sentence_bert.py`):

- **How it works**: Sentence-BERT is a bit more advanced. Instead of just looking at word frequency, it turns each article into a vector that represents the meaning of the sentence (also called an embedding). This allows the model to understand paraphrased content.
- **Cosine Similarity**: Again, we calculate cosine similarity, but this time using the sentence embeddings. Since Sentence-BERT understands context, it’s better at finding duplicates that might be reworded but mean the same thing.
- **Better Accuracy**: While slower than TF-IDF, Sentence-BERT is more accurate for finding semantically similar articles.

## Deduplication Script Workflow

- **Load Data**: First, the script loads the CSV file containing articles.
- **Calculate Similarity**: Then, it compares the articles using either TF-IDF or Sentence-BERT (you can choose which one to use).
- **Remove Duplicates**: Articles that are too similar (based on a defined threshold) are removed.
- **Save Cleaned Data**: Finally, the cleaned articles are saved to a new CSV file.

## Running the Code

### 1. Extracting Articles (`articles.py`):

To process a list of URLs and save the articles, just run:

```python
process_links_from_json('path_to_json_file.json', 'path_to_output_csv_file.csv')
```

### 2. Deduplication Using TF-IDF (`tfidf.py`):

To remove duplicates using the TF-IDF model, run:

```python
remove_duplicates_from_csv('path_to_input_csv_file.csv', 'path_to_output_csv_file.csv')
```

### 3. Deduplication Using Sentence-BERT (`sentence_bert.py`):

To remove duplicates using the Sentence-BERT model, run:

```python
remove_duplicates_with_sentence_bert('path_to_input_csv_file.csv', 'path_to_output_csv_file.csv')
```

## Results

### TF-IDF Model:

- **Speed**: Fast, but only looks at word frequency.
- **Accuracy**: It identified 76 duplicates from the dataset. It’s a good choice if speed matters more than finding semantic meaning.

### Sentence-BERT Model:

- **Speed**: A bit slower, but much more accurate.
- **Accuracy**: It also found 76 duplicates, but it did a better job of catching articles that were paraphrased or reworded.

## Summary

There are two main options for deduplication:

- **TF-IDF**: Quick and works well for articles that are worded similarly, but it might miss reworded duplicates.
- **Sentence-BERT**: Slower, but more accurate since it understands the meaning behind the words.

Use the model that best suits your needs—**TF-IDF** if you need speed, or **Sentence-BERT** if you care more about accuracy.
