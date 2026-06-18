from kafka import KafkaProducer

KAFKA_TOPIC = "news_raw"
KAFKA_SERVER = "localhost:9092"


def create_producer():
    return KafkaProducer(
        bootstrap_servers=KAFKA_SERVER,
        value_serializer=lambda value: value.encode("utf-8")
    )


def send_articles_to_kafka(articles):
    producer = create_producer()

    for article in articles:
        producer.send(KAFKA_TOPIC, article.to_json())
        print(f"Article envoyé dans Kafka : {article.title}")

    producer.flush()
    producer.close()