from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, when

spark = SparkSession.builder.appName("MediTrustQuality").getOrCreate()

df = spark.read.option("header", True).csv("/data/raw/patients.csv")

summary = df.select(
    count("*").alias("total_records"),
    count(when(col("patient_id").isNull() | (col("patient_id") == ""), True)).alias("missing_patient_ids"),
    count(when(col("full_name").isNull() | (col("full_name") == ""), True)).alias("missing_names")
)

summary.show()
spark.stop()
