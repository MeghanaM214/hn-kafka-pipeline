\# Real-Time Hacker News Data Pipeline (Kafka → S3 → Spark)
iIplemented an end-to-end real-time data ingestion pipeline that streams live data from the Hacker News API into Apache Kafka and persists raw events into Amazon S3. The stored data is then read and analyzed using Apache Spark / Databricks.

This project follows modern data engineering best practices such as decoupled ingestion, raw/bronze data storage, and scalable analytics.

Architecture:

Hacker News API

&nbsp;     ↓

Python Kafka Producer

&nbsp;     ↓

Apache Kafka (Docker)

&nbsp;     ↓

Python Kafka Consumer

&nbsp;     ↓

Amazon S3 (Raw / Bronze Layer)

&nbsp;     ↓

Apache Spark / Databricks

```



---



\## 🛠️ Tech Stack

\- \*\*Python 3.10+\*\*

\- \*\*Apache Kafka\*\*

\- \*\*Docker \& Docker Compose\*\*

\- \*\*AWS S3\*\*

\- \*\*AWS CLI \& IAM\*\*

\- \*\*Apache Spark / Databricks\*\*



---



\## 📂 Project Structure

```

hn-kafka-pipeline/

│── docker-compose.yml

│

├── producer/

│   ├── producer.py

│   └── requirements.txt

│

├── consumer/

│   ├── consumer.py

│   └── requirements.txt

│

├── s3/   # logical raw data destination

└── venv/

```



---



\## ⚙️ Setup Instructions



\### 1️⃣ Clone Repository

```bash

git clone https://github.com/<your-username>/hn-kafka-pipeline.git

cd hn-kafka-pipeline

```



\### 2️⃣ Create \& Activate Virtual Environment

```bash

python -m venv venv

venv\\Scripts\\activate  # Windows

```



\### 3️⃣ Install Dependencies

```bash

pip install -r producer/requirements.txt

pip install -r consumer/requirements.txt

```



---



\## 🚀 Running the Pipeline



\### Start Kafka (Docker)

```bash

docker-compose up -d

```



\### Create Kafka Topic

```bash

docker exec -it kafka kafka-topics.sh \\

--create --topic hackernews \\

--bootstrap-server localhost:9092 \\

--partitions 1 --replication-factor 1

```



\### Run Producer

```bash

cd producer

python producer.py

```



\### Run Consumer

```bash

cd consumer

python consumer.py

```



Data will now start appearing in \*\*Amazon S3\*\* as raw JSON files.



---



\## 📊 Reading Data Using Spark / Databricks



\### Spark (Local or Databricks Notebook)

```python

spark.read \\

&nbsp; .json("s3a://<your-bucket-name>/hackernews/") \\

&nbsp; .printSchema()

```



\### Sample Transformations

```python

df = spark.read.json("s3a://<your-bucket-name>/hackernews/")



df.select("id", "title", "by", "time").show(10, truncate=False)

```



---



\## 🧠 Key Learnings

\- Kafka decouples ingestion from storage

\- S3 acts as an immutable raw data layer

\- Spark enables scalable downstream analytics

\- Docker simplifies local infrastructure setup



---



\## 📌 Future Enhancements

\- Add schema validation (Avro / Schema Registry)

\- Implement Dead Letter Queue (DLQ)

\- Convert to Delta Lake format

\- Add monitoring with Prometheus/Grafana



---



\## 👤 Author

\*\*Meghana M\*\*  

Data Engineer



---



⭐ If you found this project useful, give it a star!





