import feedparser
from app.models import NewsArticle

RSS_URL = "https://www.lemonde.fr/rss/une.xml"


def fetch_articles():
    feed = feedparser.parse(RSS_URL)
    articles = []

    for entry in feed.entries:
        article = NewsArticle(
            title=entry.get("title", ""),
            summary=entry.get("summary", ""),
            event_date=None,
            publication_date=entry.get("published", ""),
            source="Le Monde",
            url=entry.get("link", "")
        )
        articles.append(article)

    return articles