#!/usr/bin/env python
# coding: utf-8

# In[2]:


try:

    import os
    import sys
    import uuid
    import json


    spark_version = '3.2.4'
    SUBMIT_ARGS = f'--packages ' \
                  f'org.apache.spark:spark-sql-kafka-0-10_2.12:{spark_version},' \
                  f'org.apache.kafka:kafka-clients:2.8.1 ' \
                  f'pyspark-shell'
    os.environ["PYSPARK_SUBMIT_ARGS"] = SUBMIT_ARGS
    os.environ['PYSPARK_PYTHON'] = sys.executable
    os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
        
    import findspark
    findspark.init( '/opt/spark' )
    import pyspark
    from pyspark.sql import SparkSession
    from pyspark import SparkConf, SparkContext
    from pyspark.sql.functions import col, asc, desc
    from pyspark.sql.functions import col, to_timestamp, monotonically_increasing_id, to_date, when
    from pyspark.sql.functions import *
    from pyspark.sql.types import *
    from pyspark import SparkContext, SparkConf
    from pyspark.streaming import StreamingContext


    print("ok.....")
except Exception as e:
    print("Error : {} ".format(e))


# In[3]:


spark = SparkSession \
    .builder \
    .master("spark://91.107.226.76:7077") \
    .appName("StructuredNetworkWordCount") \
    .getOrCreate()


# In[4]:


df = spark \
  .readStream \
  .format("kafka") \
  .option("kafka.bootstrap.servers", "195.201.19.174:9092") \
  .option("subscribe", "user-tracker") \
  .load()


# In[ ]:


query = df.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)") \
    .writeStream \
    .outputMode('Append')\
    .format("console") \
    .start()

query.awaitTermination()


# In[ ]:




