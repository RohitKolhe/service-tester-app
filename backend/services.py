import psycopg2
import redis
from kafka import KafkaProducer

def test_postgres(url, username, password, ssl):
    try:
        sslmode = 'require' if ssl else 'disable'  # Set SSL mode based on the input
        conn = psycopg2.connect(
            dbname='test', 
            user=username, 
            password=password, 
            host=url, 
            sslmode=sslmode  # Specify the SSL mode
        )
        cursor = conn.cursor()
        cursor.execute("SELECT 1")
        cursor.fetchone()
        conn.close()
        return "PostgreSQL connection successful"
    except Exception as e:
        raise Exception(f"PostgreSQL connection failed: {e}")

def test_redis(url, password, ssl):
    try:
        r = redis.StrictRedis(
            host=url, 
            password=password, 
            decode_responses=True, 
            ssl=ssl  # Pass the SSL parameter
        )
        r.ping()  # Test the connection
        return "Redis connection successful"
    except Exception as e:
        raise Exception(f"Redis connection failed: {e}")

def test_kafka(url, ssl):
    try:
        # Set up the configuration for the Kafka Producer
        conf = {
            'bootstrap_servers': url,
            'security_protocol': 'ssl' if ssl else 'plaintext',  # Use SSL if specified
        }

        producer = KafkaProducer(**conf)  # Pass the configuration to the producer
        # Optionally produce a test message (this requires a valid topic to be available)
        #producer.produce('test-topic', key=b'key', value=b'test-message')
        #producer.flush()  # Wait for any outstanding messages to be delivered
        producer.close()
        return "Kafka connection successful"
    except Exception as e:
        raise Exception(f"Kafka connection failed: {e}")
