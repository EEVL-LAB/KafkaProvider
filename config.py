import os

def host_addr(host,port) :
    return f"{host}:{port}"

KAFKA_HOST_LIST = [
    host_addr(os.environ["KAFKA_HOST_0"],9092),
    host_addr(os.environ["KAFKA_HOST_1"],9092),
    host_addr(os.environ["KAFKA_HOST_2"],9092)
]

KAFKA_TOPIC = os.environ["KAFKA_TOPIC"]
DYNAMODB_ENDPOINT_URL = "https://dynamodb.ap-northeast-2.amazonaws.com"
KAFKA_OFFSET_RESET = os.environ["KAFKA_OFFSET_RESET"]