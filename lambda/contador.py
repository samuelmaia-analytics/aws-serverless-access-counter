import json
import os

import boto3


dynamodb = boto3.client("dynamodb")
TABLE_NAME = os.environ["TABLE_NAME"]
COUNTER_ID = "coming-soon-page"


def lambda_handler(event, context):
    try:
        response = dynamodb.update_item(
            TableName=TABLE_NAME,
            Key={
                "counter_id": {"S": COUNTER_ID},
            },
            UpdateExpression="ADD access_count :increment",
            ExpressionAttributeValues={
                ":increment": {"N": "1"},
            },
            ReturnValues="UPDATED_NEW",
        )

        count = int(response["Attributes"]["access_count"]["N"])

        return build_response(
            200,
            {
                "message": "Acesso contabilizado com sucesso.",
                "count": count,
            },
        )
    except Exception:
        return build_response(
            500,
            {
                "message": "Não foi possível contabilizar o acesso.",
            },
        )


def build_response(status_code, body):
    return {
        "statusCode": status_code,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
        },
        "body": json.dumps(body, ensure_ascii=False),
    }
