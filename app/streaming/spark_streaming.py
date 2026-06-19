from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json
from pyspark.sql.types import StructType, StructField, StringType, DoubleType
from app.processing.cleaning import clean_news, remove_duplicates
from app.processing.enrichment import enrich_news

schema = StructType([
    StructField("title", StringType(), True),
    StructField("summary", StringType(), True),
    StructField("event_date", StringType(), True),
    StructField("publication_date", StringType(), True),
    StructField("source", StringType(), True),
    StructField("url", StringType(), True),
    StructField("verification_status", StringType(), True),
    StructField("fake_news_score", DoubleType(), True),
])



def create_spark_session():
    return SparkSession.builder \
        .appName("NewsVerificationStreaming") \
        .getOrCreate()



def main():
    spark = create_spark_session()
    spark.sparkContext.setLogLevel("WARN")

    raw_df = spark.readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", "kafka_news:29092") \
        .option("subscribe", "news_raw") \
        .option("startingOffsets", "earliest") \
        .load()

    json_df = raw_df.selectExpr("CAST(value AS STRING) as json_value")

    news_df = json_df \
        .select(from_json(col("json_value"), schema).alias("data")) \
        .select("data.*")

    clean_df = (

        clean_news(news_df)
        .filter(col("title").isNotNull()) 
        .filter(col("url").isNotNull())
    )
    clean_df = remove_duplicates(clean_df)
    enriched_df = enrich_news(clean_df)
        
        

    query = enriched_df.writeStream \
        .format("console") \
        .outputMode("append") \
        .option("truncate", "false") \
        .start()

    query.awaitTermination()


if __name__ == "__main__":
    main()