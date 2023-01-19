import boto3

from boto3.dynamodb.conditions import Key, Attr


dynamodb = boto3.resource('dynamodb','ap-southeast-2')


table = dynamodb.Table('ga4_offline_event')

event_list = ["web_login", "account_activation", "paying_org", "user_created"]

date_list = ["2023-01-01","2023-01-02","2023-01-03","2023-01-04","2023-01-05","2023-01-06","2023-01-07","2023-01-08","2023-01-09","2023-01-10","2023-01-11"]

for date_list_item in date_list:
    print("---------------------------\n")
    print(date_list_item)
    for event_list_item in event_list:
        response = table.query(KeyConditionExpression=Key('event_name').eq(event_list_item) & Key('event_time').begins_with(date_list_item) )
        print("{} {}".format(event_list_item,response.get('Count')))

        

        
import boto3

from boto3.dynamodb.conditions import Key, Attr


dynamodb = boto3.resource('dynamodb','ap-southeast-2')


table = dynamodb.Table('ga4_offline_event')

response = table.scan(FilterExpression=Attr("event_name").eq("user_created") & Attr("event_time").begins_with("2023-01-17") )
#print (response)
print(response.get('Count'))



import boto3
dynamo = boto3.resource('dynamodb','ap-southeast-2')

def truncateTable(tableName):
    table = dynamo.Table(tableName)

    #get the table keys
    tableKeyNames = [key.get("AttributeName") for key in table.key_schema]

    #Only retrieve the keys for each item in the table (minimize data transfer)
    projectionExpression = "#g,#e "
    expressionAttrNames = {'#g':'gaClientId','#e':'eventName'}

    counter = 0
    page = table.scan(ProjectionExpression=projectionExpression, ExpressionAttributeNames=expressionAttrNames)
    with table.batch_writer() as batch:
        while page["Count"] > 0:
            counter += page["Count"]
            # Delete items in batches
            for itemKeys in page["Items"]:
                batch.delete_item(Key=itemKeys)
            # Fetch the next page
            if 'LastEvaluatedKey' in page:
                page = table.scan(
                    ProjectionExpression=projectionExpression, ExpressionAttributeNames=expressionAttrNames,
                    ExclusiveStartKey=page['LastEvaluatedKey'])
            else:
                break
    print(f"Deleted {counter}")

truncateTable("GA_Record")
