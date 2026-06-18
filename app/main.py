from app.scrapers.gorafi import fetch_articles as fetch_gorafi_articles
from app.scrapers.lemonde import fetch_articles as fetch_lemonde_articles
from app.scrapers.afp_factcheck import fetch_articles as fetch_afp_factcheck_articles

def main():
    articles = []

    gorafi_articles = fetch_gorafi_articles()
    lemonde_articles = fetch_lemonde_articles()
    afp_articles = fetch_afp_factcheck_articles()


    articles.extend(gorafi_articles)
    articles.extend(lemonde_articles)
    articles.extend(afp_articles)

    print(f"Nombre total d'articles collectés : {len(articles)}")

    for article in articles[:10]:
        print("-" * 50)
        print(article.to_dict())


if __name__ == "__main__":
    main()