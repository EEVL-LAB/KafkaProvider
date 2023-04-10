import boto3

ENDPOINT_URL = "http://localhost:8888"


resource = boto3.resource('dynamodb', endpoint_url=ENDPOINT_URL)
client = boto3.client('dynamodb', endpoint_url=ENDPOINT_URL)

table = resource.Table("TestTable")