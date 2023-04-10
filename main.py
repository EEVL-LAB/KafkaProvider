from aiokafka import AIOKafkaConsumer
import asyncio
import config
import json

loop = asyncio.get_event_loop()

async def consume():
    consumer = AIOKafkaConsumer(
        config.KAFKA_TOPIC,
        loop=loop,
        group_id='scraping_consummer_dev',
        bootstrap_servers=config.KAFKA_HOST_LIST,
        auto_offset_reset='earliest',
        value_deserializer=lambda x: json.loads(x.decode('utf-8')),
        enable_auto_commit=False
    )
    print("-"*10)
    print(f"[INFO] KAFKA CONSUMMER INIT MODE - {config.MODE}")
    print(f"[INFO] TOPIC : {config.KAFKA_TOPIC}")
    print(f"[INFO] HOSTS : {config.KAFKA_HOST_LIST}")
    print("-"*10)
    await consumer.start()
    try:
        async for msg in consumer:
            document = msg.value
            print(document.get("title"))
    finally:
        await consumer.stop()

loop.run_until_complete(consume())