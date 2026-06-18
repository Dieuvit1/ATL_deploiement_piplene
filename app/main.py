from app.scrapers.gorafi import fetch_articles as fetch_gorafi_articles
from app.scrapers.lemonde import fetch_articles as fetch_lemonde_articles
from app.scrapers.afp_factcheck import fetch_articles as fetch_afp_factcheck_articles
from app.producers.kafka_producer import send_articles_to_kafka


def main():
    articles = []

    articles.extend(fetch_gorafi_articles())
    articles.extend(fetch_lemonde_articles())
    articles.extend(fetch_afp_factcheck_articles())

    print(f"Nombre total d'articles collectés : {len(articles)}")

    send_articles_to_kafka(articles)


if __name__ == "__main__":
    main()