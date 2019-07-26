# Push AWS CloudTrail Logs to Fluentd EC2 in private VPC
get cloudtrail log from the s3 event notification and get them shipped into fluentd

## Description
AWS CloudTrail is a service that enables governance, compliance, operational auditing, and risk auditing of your AWS account. With CloudTrail, you can log, continuously monitor, and retain account activity related to actions across your AWS infrastructure. CloudTrail provides event history of your AWS account activity, including actions taken through the AWS Management Console, AWS SDKs, command line tools, and other AWS services.

By default, CloudTrail logs are aggregated per region and then redirected to an S3 bucket (compressed JSON files). You can then use the recorded logs to analyze calls and take action accordingly. 
Analyzing hundreds or thousand of data every day is the real challange.

Aggregating these logs into your existing ELK or EFK solution will allow you to tackle this challenge by giving you the ability to analyze and visualize the data.

## Objectives

* aggregate logs into a single location
* parse and enrich data
* visualize important event activity
* get warned for an alert and react faster 

## Architecture
![cloudtraillambda](https://github.com/ridowidi/images/blob/master/cloudtraillambda.png)


## How to Install
- clone this repo
- change your current working directory
```cd cloudtrail-lambda```
- Install python dependency libraries
```pip install -r requirements.txt -t ./```
- Zip this bundle of joy, a zip format is always a more convenient way for uploading the code into AWS lambda dashboard
```zip -r ../cloudtraillambda.zip .```

## Additional Configuration Required on AWS Lambda
TODO 
