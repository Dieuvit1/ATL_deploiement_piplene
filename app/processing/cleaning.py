from pyspark.sql.functions import trim, lower, col


def clean_news(df):
    """
    Nettoyage des articles.
    """

    return (
        df
        .withColumn("title", trim(col("title")))
        .withColumn("summary", trim(col("summary")))
        .withColumn("source", trim(col("source")))
        .withColumn("url", trim(col("url")))
        .withColumn("source_normalized", lower(col("source")))
    )

def remove_duplicates(df):
    """
    Supprime les doublons sur l'URL.
    """

    return df.dropDuplicates(["url"])