import feedparser
from app.models import NewsArticle

RSS_URL = "https://www.legorafi.fr/feed/"


def fetch_articles():
    feed = feedparser.parse(RSS_URL)
    articles = []

    for entry in feed.entries:
        article = NewsArticle(
            title=entry.get("title", ""),
            summary=entry.get("summary", ""),
            event_date=None,
            publication_date=entry.get("published", ""),
            source="Le Gorafi",
            url=entry.get("link", "")
        )
        articles.append(article)

    return articles


if __name__ == "__main__":
    articles = fetch_articles()

    print(f"{len(articles)} articles récupérés\n")

    for article in articles[:5]:
        print("-" * 50)
        print("Titre :", article.title)
        print("Date :", article.publication_date)
        print("Lien :", article.url)