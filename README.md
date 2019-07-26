# cloudtrail-lambda
get cloudtrail log from the s3 event notification and get them shipped into fluentd

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
