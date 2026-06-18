import feedparser

RSS_URL = "https://www.legorafi.fr/feed/"


def fetch_articles():
    """
    Récupère les derniers articles publiés sur Le Gorafi via son flux RSS.
    """
    feed = feedparser.parse(RSS_URL)

    articles = []

    for entry in feed.entries:
        article = {
            "title": entry.get("title", ""),
            "summary": entry.get("summary", ""),
            "published": entry.get("published", ""),
            "link": entry.get("link", ""),
            "source": "Le Gorafi"
        }

        articles.append(article)

    return articles


if __name__ == "__main__":

    articles = fetch_articles()

    print(f"{len(articles)} articles récupérés\n")

    for article in articles[:5]:
        print("-" * 50)
        print("Titre :", article["title"])
        print("Date :", article["published"])
        print("Lien :", article["link"])