"""Forex data processing using PySpark."""
from os.path import abspath

from pyspark.sql import SparkSession
from pyspark.sql.functions import col

warehouse_location = abspath("spark-warehouse")

# Initialize Spark Session
spark = (
    SparkSession.builder
    .appName("Forex processing")
    .config("spark.sql.warehouse.dir", warehouse_location)
    .enableHiveSupport()
    .getOrCreate()
)

# Read the file forex_rates.json from the HDFS
df = spark.read.json("hdfs://namenode:9000/forex_data/forex_rates.json")

# Drop the duplicated rows based on the base and last_update columns
forex_rates = (
    df.select(
        col("base"),
        col("last_update"),
        col("rates.eur"),
        col("rates.usd"),
        col("rates.cad"),
        col("rates.gbp"),
        col("rates.jpy"),
        col("rates.nzd"),
    )
    .dropDuplicates(["base", "last_update"])
    .fillna(0, subset=["eur", "usd", "cad", "gbp", "jpy", "nzd"])
)

# Export the dataframe into the Hive table forex_rates
forex_rates.write.mode("append").insertInto("forex_rates")
