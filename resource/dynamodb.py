import boto3
import config

class DynamoDB:
    def __init__(self) -> None:
        self.resource = boto3.resource('dynamodb', endpoint_url=config.DYNAMODB_ENDPOINT_URL)
        self.client = boto3.client('dynamodb', endpoint_url=config.DYNAMODB_ENDPOINT_URL)
        self.table = self.resource.Table("ScrapingData")
        
    def check_saved(self,item:dict) -> bool :
        print(item)
        data = self.get_data(item)
        return True if data.get("Item") else False
        
    def insert_data(self,item):
        if self.check_saved(item) :
            print(f"[INFO] Already Saved Data In DynamoDB : {item['TargetKeyword']},{item['CRC']}")
        
        else :
            put_resp = self.table.put_item(Item=item)
            print(f"[INFO] Insert Data In DynamoDB : {item['TargetKeyword']},{item['CRC']}")
    
    def get_data(self,item) :
        data = self.table.get_item(
            Key={
                'TargetKeyword': item["TargetKeyword"],
                'CRC': item["CRC"]
            }
        )
        return data