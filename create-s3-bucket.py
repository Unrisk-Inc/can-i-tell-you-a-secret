import boto3

ACCESS_KEY = "AKIAVDLEKJZGJEWT6NWG"
SECRET_KEY = "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"

# Create an S3 client
s3 = boto3.client(
    's3',
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY
)

# Call S3 to list current buckets
response = s3.list_buckets()

# Get a list of all bucket names from the response
buckets = [bucket['Name'] for bucket in response['Buckets']]

# Print out the bucket list
print("Bucket List: %s" % buckets)