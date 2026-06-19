import feedparser
from app.models import NewsArticle

RSS_URL = "https://factuel.afp.com/rss.xml"


def fetch_articles():
    feed = feedparser.parse(RSS_URL)
    articles = []

    for entry in feed.entries:
        article = NewsArticle(
            title=entry.get("title", ""),
            summary=entry.get("summary", ""),
            event_date=None,
            publication_date=entry.get("published", ""),
            source="AFP Factuel",
            url=entry.get("link", ""),
            verification_status="verified_source"
        )
        articles.append(article)

    return articles