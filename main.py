from secrets import access_key, secret_access_key
import boto3

client = boto3.client('s3',
                      aws_access_key_id=access_key,
                      aws_secret_access_key=secret_access_key)

resp = client.list_objects_v2(Bucket='maxims-bucket-1')
keys = []

for obj in resp['Contents']:
    keys.append(obj['Key'])

resource = boto3.resource('s3',
                          aws_access_key_id=access_key,
                          aws_secret_access_key=secret_access_key)

for key in keys:
    copy_source = {
        'Bucket': 'maxims-bucket-1',
        'Key': key
    }
    bucket = resource.Bucket('maxims-bucket-2')
    bucket.copy(copy_source, key)