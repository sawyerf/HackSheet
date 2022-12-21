<picture>
    <source height="100px" srcset="https://user-images.githubusercontent.com/22857002/173680216-a56be2b1-a2d0-4ca9-8739-40f08b0d487e.svg#gh-dark-mode-only" media="(prefers-color-scheme: dark)">
    <img height="100px" src="https://user-images.githubusercontent.com/28403617/172728814-0628eea3-922e-4011-8411-51c562f4e576.svg#gh-light-mode-only">
</picture>

---

- [AWS](#aws)
- [Kubernetes](#kubernetes)

# AWS

[aws cli documentation](https://docs.aws.amazon.com/cli/latest/reference/index.html)

### Configure
```
aws configure

AWS Access Key ID [None]: key_id
AWS Secret Access Key [None]: access_key
Default region name [None]: eu-west-3 
Default output format [None]:
```

> Note: If you have a multiple of account you can specifie your account and your endpoint url with `--profile <profile_name>` and `--endpoint-url <url>`.

<strong>Example:</strong>

```bash
aws --profile <profile> --endpoint-url <url> iam list-attached-user-policies --user-name <USERNAME>
```

## IAM

[aws iam documentation](https://docs.aws.amazon.com/cli/latest/reference/iam/index.html#cli-aws-iam)

### List policies attached to an user
```bash
aws iam list-attached-user-policies --user-name <USERNAME>
```

This command will return an object like this:

```json
{
  "AttachedPolicies": [
      {
          "PolicyName": "<POLICY_NAME>",
          "PolicyArn": "arn:aws:iam::......:policy/<POLICY_NAME>"
      }
  ],
  "IsTruncated": false
}
```

### Get policy detail from an policy arn

```bash
aws iam get-policy --policy-arn <ARN_POLICY>
```

### List user policy

```bash
aws iam list-user-policies --user-name <USER_NAME>
```

### Get user policy detail for an user

```bash
aws iam get-user-policy --user-name <USER_NAME> --policy-name <POLICY_NAME>
```

## LAMBDA

[aws lambda documentation](https://docs.aws.amazon.com/cli/latest/reference/lambda/index.html)

### List function

```bash
aws lambda list-functions
```

### Get public url of the function

```bash
aws lambda get-function-url-config --function-name <FUNCTION_NAME>
```

## S3

[aws s3 documentation](https://docs.aws.amazon.com/cli/latest/reference/s3/index.html)
[aws s3api documentation](https://docs.aws.amazon.com/cli/latest/reference/s3api/index.html)


### List buckets
```bash
aws s3api list-buckets --query "Buckets"
```

### List object in buckets
```bash
aws s3api list-objects --bucket <BUCKET>
```

### List bucket files
```bash
aws s3 ls --recursive s3://<bucket_name>
```

### Get file from bucket
```bash
aws s3 sync s3://<bucket_name> <destination>
```

### Upload file to bucket
```bash
aws s3 cp <path_to_file> s3://<bucket_name>
```

## Dynamodb

[aws dynamodb documentation](https://docs.aws.amazon.com/cli/latest/reference/dynamodb/index.html)

### List all tables
```bash
aws dynamodb list-tables
```

### Get data from table
```bash
aws dynamodb scan --table-name <table_name>
```

### Create table
```bash
aws --endpoint-url http://localhost:4566 dynamodb create-table --table-name example \
  --attribute-definitions AttributeName=example_attribute,AttributeType=S \
  --key-schema AttributeName=example_attribute,KeyType=HASH \
  --provisioned-throughput ReadCapacityUnits=10, WriteCapacityUnits=5
```

### Put item in table
```bash
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
