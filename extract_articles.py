import json
import csv
import uuid
from newspaper import Article

def get_article_content(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        
        title = article.title if article.title else "No title found"
        article_content = article.text if article.text else "No article content found"
        
        return title, article_content
        
    except Exception as e:
        print(f"Error processing the URL {url}: {str(e)}")
        return "No title found", None

def process_links_from_json(json_file, output_csv_file):
    with open(json_file, 'r') as file:
        data = json.load(file)
    
    links = data.get("urls", [])
    
    with open(output_csv_file, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['id', 'article', 'highlights']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        
        for link in links:
            print(f"Processing: {link}")
            title, article_content = get_article_content(link)
            
            if article_content is None:
                continue
            
            unique_id = str(uuid.uuid4())
            
            writer.writerow({
                'id': unique_id,
                'article': article_content,
                'highlights': title
            })
            print(f"Article: {title[:100]}...")
            print("-" * 80)

process_links_from_json('D:/Newspaper_DeduplicationCopy/linkstonews.json', 'D:/Newspaper_DeduplicationCopy/articles.csv')
