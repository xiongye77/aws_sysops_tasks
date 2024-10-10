import json
import csv
import boto3
import os
import tempfile
import uuid

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    try:
        # Extract bucket and key from the event input
        bucket = event['bucket']
        key = event['key']
        print (bucket)
        print (key)
        # Download the JSON file from S3
        download_path = os.path.join(tempfile.gettempdir(), uuid.uuid4().hex)
        s3_client.download_file(bucket, key, download_path)

        # Read JSON data
        with open(download_path, 'r') as json_file:
            data = json.load(json_file)
         
            print (data)
            flattened_data = []

        # Iterate over each customer
            for customer in data.get('customers', []):
                customer_id = customer.get('customerId')
                # Extract customer information
                customer_info = {
                    'customerId': customer_id,
                    'firstName': customer.get('firstName'),
                    'lastName': customer.get('lastName'),
                    'email': customer.get('email'),
                    'phone': customer.get('phone'),
                    'dateOfBirth': customer.get('dateOfBirth'),
                    'accountStatus': customer.get('accountStatus'),
                    'loyaltyPoints': customer.get('loyaltyPoints'),
                }
    
                # Extract address information
                address = customer.get('address', {})
                address_info = {
                    'street': address.get('street'),
                    'city': address.get('city'),
                    'state': address.get('state'),
                    'postalCode': address.get('postalCode'),
                    'country': address.get('country'),
                }
    
                # Merge customer and address information
                customer_address_info = {**customer_info, **address_info}
    
                # Iterate over purchase history
                purchase_history = customer.get('purchaseHistory', [])
                if purchase_history:
                    for purchase in purchase_history:
                        # Extract purchase information
                        purchase_info = {
                            'purchaseId': purchase.get('purchaseId'),
                            'purchaseDate': purchase.get('date'),
                            'totalAmount': purchase.get('totalAmount'),
                            'paymentMethod': purchase.get('paymentMethod'),
                        }
    
                        # Iterate over items in the purchase
                        items = purchase.get('items', [])
                        if items:
                            for item in items:
                                # Extract item information
                                item_info = {
                                    'productId': item.get('productId'),
                                    'productName': item.get('productName'),
                                    'quantity': item.get('quantity'),
                                    'price': item.get('price'),
                                }
    
                                # Combine all information into one record
                                record = {**customer_address_info, **purchase_info, **item_info}
                                flattened_data.append(record)
                        else:
                            # No items in the purchase, but we still want to record the purchase
                            record = {**customer_address_info, **purchase_info}
                            flattened_data.append(record)
                else:
                    # No purchase history, but we still want to record the customer information
                    flattened_data.append(customer_address_info)
    
            # [Include your JSON parsing and flattening logic here]

        # For illustration, let's assume 'data' is already in the desired format
        

        # Determine all fieldnames
        fieldnames = set()
        for record in flattened_data:
            fieldnames.update(record.keys())
        fieldnames = sorted(fieldnames)

        # Write flattened data to CSV
        csv_file_name = 'flattened_data.csv'
        csv_file_path = os.path.join(tempfile.gettempdir(), csv_file_name)
        with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for record in flattened_data:
                writer.writerow(record)

        # Upload CSV to S3
        output_location = os.environ.get('OUTPUT_LOCATION')
        csv_key = os.path.join(output_location, f'{uuid.uuid4().hex}_{csv_file_name}')
        s3_client.upload_file(csv_file_path, bucket, csv_key)

        # Return the CSV S3 URI
        csv_s3_uri = f's3://{bucket}/{csv_key}'
        return {
            'statusCode': 200,
            'csvS3Uri': csv_s3_uri
        }

    except Exception as e:
        print(f"Error processing file {key} from bucket {bucket}.")
        print(e)
        return {
            'statusCode': 500,
            'error': str(e)
        }
