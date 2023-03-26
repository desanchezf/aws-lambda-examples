import json
import requests


def get_users(event, context):

    ## Realizamos la llamada a la API de neuromobile






    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "retorno de los usuarios",
        }),
    }

def get_events(event, context):

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "retorno de los eventos",
        }),
    }