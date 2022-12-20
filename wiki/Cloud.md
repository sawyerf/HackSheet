<picture>
    <source height="100px" srcset="https://user-images.githubusercontent.com/22857002/173680216-a56be2b1-a2d0-4ca9-8739-40f08b0d487e.svg#gh-dark-mode-only" media="(prefers-color-scheme: dark)">
    <img height="100px" src="https://user-images.githubusercontent.com/28403617/172728814-0628eea3-922e-4011-8411-51c562f4e576.svg#gh-light-mode-only">
</picture>

---

- [AWS](#aws)
- [Kubernetes](#kubernetes)
- [Azure](#azure)

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

# Kubernetes

> Kubernetes commonly stylized as K8s is an open-source container orchestration system for automating software deployment, scaling, and management. Google originally designed Kubernetes, but the Cloud Native Computing Foundation now maintains the project. 

### Usefull paths


```
/run/secrets/kubernetes.io/serviceaccount/ca.crt
/run/secrets/kubernetes.io/serviceaccount/namespace
/run/secrets/kubernetes.io/serviceaccount/token

/var/run/secrets/kubernetes.io/serviceaccount/ca.crt
/var/run/secrets/kubernetes.io/serviceaccount/namespace
/var/run/secrets/kubernetes.io/serviceaccount/token
```

### Namespace

```
kubectl get namespace --server <HOST> --certificate-authority=ca.crt --token=$token
```

### Authorization

```
kubectl auth can-i --list --namespace=<NAMESPACES> --server <HOST> --certificate-authority=ca.crt --token=$token
```

### Secrets

List all secrets:
```
kubectl get secrets --namespace=<NAMESPACES> --server <HOST> --certificate-authority=ca.crt --token=$token
```

Get secret:

```
kubectl describe secret <SECRET-ID> --namespace=<NAMESPACE> --server <HOST> --certificate-authority=ca.crt --token=$token
```

### Pods

Get:

```
kubectl --namespace=<NAMESPACE> --server <HOST> --certificate-authority=ca.crt --token=$token get pods
```

Describe:

You can get configuration of specific
```
kubectl --namespace=<NAMESPACE> --server <HOST> --certificate-authority=ca.crt --token=$token describe pod <POD_ID>
```

Apply:

If you have good rights to apply a pod, most of the time you will be able to turn up the volume of the root machine.

You can find an definition of malicious pod here: [pwn.yml](https://github.com/sawyerf/HackSheet/blob/main/scripts/pwn.yml)

```
kubectl --namespace=<NAMESPACE> --server <HOST> --certificate-authority=ca.crt --token=$token apply -f pwn.yml
```

### Exec command

```
kubectl --namespace=<NAMESPACE> --server <HOST> --certificate-authority=ca.crt --token=$token exec -it pwn -- bash
```

### Usefull link

- [Kubernetes Methodology 1](https://www.cyberark.com/resources/threat-research-blog/kubernetes-pentest-methodology-part-1)
- [Kubernetes Methodology 2](https://www.cyberark.com/resources/threat-research-blog/kubernetes-pentest-methodology-part-2)
- [Pods PE](https://bishopfox.com/blog/kubernetes-pod-privilege-escalation)

# Azure

## Domain name for Azure resources storages

- Blob storage -> <strong>https://[account].blob.core.windows.net</strong>
- Azure Data Lake Storage Gen2 -> <strong>https://[account].dfs.core.windows.net</strong>
- Azure files -> <strong>https://[account].file.core.windows.net</strong>
- Queue storage -> <strong>https://[account].queue.core.windows.net</strong>
- Table storage -> <strong>https://[account].table.core.windows.net</strong>


## List public blob


#### List all containers files.
```bash
curl http://<account>.blob.core.windows.net/<container>?restype=container&comp=list&se=<SE>&sp=<SP>&sv=<SV>&sr=c&sig=<SIG>%3D
```

#### List one file
```bash
curl "http://<account>.blob.core.windows.net/<container>/<file_name>?se=<SE>&sp=rl&sv=<SV>&sr=c&sig=<SIG>%3D"
```

> Note %3D is '=' and it's required

[Here you can find more information for query parameters](https://learn.microsoft.com/en-us/rest/api/storageservices/create-service-sas#service-sas-example)


## Azure cosmos

#### List table content

```py
# script.py
from azure.cosmosdb.table import TableService

table_service = TableService(account_name="...", sas_token='se=<SE>&sp=<SP>&sv=<SV>&tn=<Table>&sig=<SIG>%3D', protocol='http', endpoint_suffix='core.windows.net')
print(table_service.exists('<TABLE>'))
print(list(table_service.query_entities('<TABLE>')))
```