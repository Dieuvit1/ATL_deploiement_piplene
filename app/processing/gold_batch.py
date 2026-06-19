from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, lit


def create_spark_session():
    return SparkSession.builder \
        .appName("NewsGoldBatch") \
        .getOrCreate()


def main():
    spark = create_spark_session()
    spark.sparkContext.setLogLevel("WARN")

    silver_path = "/opt/project/data/silver/news"
    gold_path = "/opt/project/data/gold/news"

    df = spark.read.parquet(silver_path)

    gold_df = (
        df
        .withColumn(
            "fake_news_score",
            when(col("source_normalized") == "le gorafi", lit(0.95))
            .when(col("source_normalized") == "afp factuel", lit(0.05))
            .when(col("source_normalized") == "le monde", lit(0.20))
            .otherwise(lit(0.50))
        )
        .withColumn(
            "verification_status",
            when(col("fake_news_score") >= 0.80, lit("suspect"))
            .when(col("fake_news_score") <= 0.20, lit("likely_verified"))
            .otherwise(lit("to_review"))
        )
    )

    gold_df.write \
        .mode("overwrite") \
        .parquet(gold_path)

    print("Couche Gold générée avec succès.")


if __name__ == "__main__":
    main()