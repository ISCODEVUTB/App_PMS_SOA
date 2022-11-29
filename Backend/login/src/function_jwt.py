from jwt import encode, decode, exceptions
from flask import jsonify
from datetime import datetime, timedelta
from os import getenv


def expire_date(day: int):
    now = datetime.now()
    new = now + timedelta(days=day)
    return new


def write_token(data: dict):
    token = encode(payload={**data, "exp": expire_date(2)}, key=getenv("SECRET"), algorithm="HS256")
    token.encode("UTF-8")
    return token


def validate_token(token, output=False):
    try:
        if output:
            return decode(token, key=getenv("SECRET"), algorithms=["HS256"])
        else:
            decode(token, key=getenv("SECRET"), algorithms=["HS256"])
    except exceptions.DecodeError:
        response = jsonify({"Message": "Invalid Token"})
        response.status_code = 401
        return response
    except exceptions.ExpiredSignatureError:
        response = jsonify({"Message": "Token Expired"})
        response.status_code = 401
        return response

