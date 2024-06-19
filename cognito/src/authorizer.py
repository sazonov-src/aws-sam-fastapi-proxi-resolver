def handler(event, context):
    token = event["headers"].get("Authorization")
    # Implement your token validation logic here
    print(event)
    return {
        "policyDocument": {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Action": "execute-api:Invoke",
                    "Effect": "Deny",
                    "Resource": event["methodArn"],
                }
            ],
        },
        }
