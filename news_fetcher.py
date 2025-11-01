#allows the code to use the requests and datetime library 
import requests
from datetime import datetime

#Key and URL so the code can use it 
API_KEY = ""  
NEWS_URL = "https://newsapi.org/v2/everything"

#the function sets up the parameters for the API
def get_news(topic):
    params = {
        "q": topic,
        "pageSize": 5,
        "language": "en",
        "sortBy": "publishedAt",
        "apiKey": API_KEY
    }
    response = requests.get(NEWS_URL, params=params)
    
    #checks if the API works 
    if response.status_code == 200:
        return response.json().get("articles", [])
    else:
        print("Error:", response.status_code)
        return []

#this function allows us to call the API and get the info from it
def parse_article(article, i):
    title = article.get("title", "No title")
    description = article.get("description", "No description")
    published_at = article.get("publishedAt", "")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"\n{i}. Title: {title}")
    print(f"   Description: {description}")
    print(f"   Published At: {published_at}")
    print(f"   Fetched At: {timestamp}")

    return {
        "timestamp": timestamp,
        "title": title,
        "description": description,
        "published_at": published_at
    }

#this function logs the call from the parse_article function and saves to a txt file
def log_news(entry, filename="news_log.txt"):
    with open(filename, "a", encoding="utf-8") as f:
        f.write(
            f"Timestamp: {entry['timestamp']}\n"
            f"Title: {entry['title']}\n"
            f"Description: {entry['description']}\n"
            f"Published At: {entry['published_at']}\n"
            f"{'-'*60}\n"
        )
    print(f"News saved to {filename}")

#this functions allows the user to input the topic 
def main():
    topic = input("Enter news topic: ")
    articles = get_news(topic)

    if not articles:
        print("No articles found.")
        return

    for i, article in enumerate(articles, 1):
        entry = parse_article(article, i)
        log_news(entry)


if __name__ == "__main__":
    main()
