from pyspark.sql import SparkSession
from pyspark.sql.functions import col, regexp_replace, trim, to_timestamp


def create_spark_session():
    return SparkSession.builder \
        .appName("NewsSilverBatch") \
        .getOrCreate()


def main():
    spark = create_spark_session()
    spark.sparkContext.setLogLevel("WARN")

    bronze_path = "/opt/project/data/bronze/news"
    silver_path = "/opt/project/data/silver/news"

    df = spark.read.parquet(bronze_path)

    silver_df = (
        df
        .withColumn("summary_clean", regexp_replace(col("summary"), "<[^>]*>", ""))
        .withColumn("summary_clean", regexp_replace(col("summary_clean"), "\\n", " "))
        .withColumn("summary_clean", trim(col("summary_clean")))
        .withColumn("title_clean", trim(col("title")))
        .withColumn("publication_timestamp", to_timestamp(col("publication_date")))
        .dropDuplicates(["article_id"])
    )

    silver_df.write \
        .mode("overwrite") \
        .parquet(silver_path)

    print("Couche Silver générée avec succès.")


if __name__ == "__main__":
    main()