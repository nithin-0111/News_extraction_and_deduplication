import json
import csv
import uuid
from newspaper import Article

def get_article_content(url):
    """
    This function uses the newspaper3k library to extract the article content and highlights (title).
    """
    try:
        # Create an Article object and download the article
        article = Article(url)
        article.download()
        article.parse()
        
        # Extract title and article content
        title = article.title if article.title else "No title found"
        article_content = article.text if article.text else "No article content found"
        
        return title, article_content
        
    except Exception as e:
        # Handle errors gracefully and log them
        print(f"Error processing the URL {url}: {str(e)}")
        return "No title found", None

def process_links_from_json(json_file, output_csv_file):
    """
    This function processes URLs from a JSON file, extracts the articles and titles,
    and writes them into a CSV file.
    """
    # Load links from JSON
    with open(json_file, 'r') as file:
        data = json.load(file)
    
    links = data.get("urls", [])
    
    # Open CSV file for writing
    with open(output_csv_file, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['id', 'article', 'highlights']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()  # Write CSV header
        
        for link in links:
            print(f"Processing: {link}")
            title, article_content = get_article_content(link)
            
            # If there's no content, skip this link
            if article_content is None:
                continue
            
            # Generate a unique ID
            unique_id = str(uuid.uuid4())
            
            # Write data to CSV
            writer.writerow({
                'id': unique_id,
                'article': article_content,
                'highlights': title
            })
            print(f"Article: {title[:100]}...")  # Print first 100 characters of the title as preview
            print("-" * 80)

# Example usage: Modify the JSON file path and output CSV file path accordingly
process_links_from_json('D:/Newspaper_DeduplicationCopy/linkstonews.json', 'D:/Newspaper_DeduplicationCopy/articles.csv')
