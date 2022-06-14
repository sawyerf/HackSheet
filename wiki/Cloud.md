<picture>
    <source height="100px" srcset="https://user-images.githubusercontent.com/28403617/172728813-44af208a-978d-4ef1-a6e6-ff724d5baf0f.svg" media="(prefers-color-scheme: dark)">
    <img height="100px" src="https://user-images.githubusercontent.com/28403617/172728814-0628eea3-922e-4011-8411-51c562f4e576.svg#">
</picture>

---

- [AWS](#aws)

# AWS
### Configure
```
aws configure

AWS Access Key ID [None]: key_id
AWS Secret Access Key [None]: access_key
Default region name [None]: eu-west-3 
Default output format [None]:
```

## S3
### List bucket
```
aws --profile <profile> --endpoint-url <url> s3api list-buckets --query "Buckets"
```

### List bucket files
```
aws --profile <profile> --endpoint-url <url> s3 ls --recursive s3://<bucket_name>
```

### Get file from bucket
```
aws --profile <profile> --endpoint-url <url> s3 sync s3://<bucket_name> <destination>
```

### Upload file to bucket
```
aws --profile <profile> --endpoint-url <url> s3 cp <path_to_file> s3://<bucket_name>
```

## Dynamodb
### List all tables
```
aws --profile <profile> --endpoint-url <url> dynamodb list-tables
```

### Get data from table
```
aws --profile <profile> --endpoint-url <url> dynamodb scan --table-name <table_name>
```

### Create table
```
aws --endpoint-url http://localhost:4566 dynamodb create-table --table-name example \
  --attribute-definitions AttributeName=example_attribute,AttributeType=S \
  --key-schema AttributeName=example_attribute,KeyType=HASH \
  --provisioned-throughput ReadCapacityUnits=10, WriteCapacityUnits=5
```

### Put item in table
```
aws --endpoint-url http://localhost:4566 dynamodb put-item --table-name example \
  --item '{"example_attribute":{"S":"Example"}}'
```