import os

def host_addr(host,port) :
    return f"{host}:{port}"

MODE = os.environ["MODE"]
KAFKA_HOST_LIST = [host_addr(os.environ["KAFKA_HOST"],9092)]

if MODE == "dev" :
    KAFKA_HOST_LIST = [
        host_addr(os.environ["KAFKA_HOST_0"],9094),
        host_addr(os.environ["KAFKA_HOST_1"],9094),
        host_addr(os.environ["KAFKA_HOST_2"],9094)
    ]

KAFKA_TOPIC = os.environ["KAFKA_TOPIC"]