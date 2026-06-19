from pyspark.sql.functions import current_timestamp, length, sha2, concat_ws


def enrich_news(df):
    """
    Ajoute des métadonnées utiles aux articles.
    """

    return (
        df
        .withColumn("title_length", length("title"))
        .withColumn("summary_length", length("summary"))
        .withColumn("processing_timestamp", current_timestamp())
        .withColumn("article_id", sha2(concat_ws("||", "source", "title", "url"), 256))
    )