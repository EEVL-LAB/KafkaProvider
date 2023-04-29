from aiokafka import AIOKafkaConsumer
from resource import ddb
import asyncio
import config
import json

loop = asyncio.get_event_loop()

async def change_ddb_data(producer_data) :
    ddb_data = {
        "URL": producer_data["url"],
        "Date": producer_data["date"],
        "Title": producer_data["title"],
        "Cotents": producer_data["contents"],
        "CotentPlainText": producer_data["content_plain_text"],
        "Thumbnails": producer_data["thumbnails"],
        "TargetKeyword": producer_data["target_keyword"],
        "ChannelKeyname": producer_data["channel_keyname"],
        "CRC": int(producer_data["crc"])
    }
    return ddb_data

async def consume():
    consumer = AIOKafkaConsumer(
        config.KAFKA_TOPIC,
        loop=loop,
        group_id=f'scraping_consummer',
        bootstrap_servers=config.KAFKA_HOST_LIST,
        auto_offset_reset=config.KAFKA_OFFSET_RESET,
        value_deserializer=lambda x: json.loads(x.decode('utf-8')),
        enable_auto_commit=False
    )
    print("-"*10)
    print(f"[INFO] KAFKA CONSUMMER INIT")
    print(f"[INFO] TOPIC : {config.KAFKA_TOPIC}")
    print(f"[INFO] HOSTS : {config.KAFKA_HOST_LIST}")
    print("-"*10)
    await consumer.start()
    try:
        async for msg in consumer:
            producer_data = msg.value
            ddb_data = await change_ddb_data(producer_data)
            ddb.insert_data(ddb_data)
    finally:
        await consumer.stop()

loop.run_until_complete(consume())