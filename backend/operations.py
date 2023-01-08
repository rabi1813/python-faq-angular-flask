import json

from decimal import Decimal
from datetime import date, datetime


def json_serializer(value):
    if isinstance(value, Decimal):
        return value.__str__()
    elif isinstance(value, (date, datetime)):
        return value.__str__()
        # return value.isoformat()


def get_data_type(connection):
    with connection.cursor() as cursor:
        query = "SELECT * FROM test_data_type;"
        cursor.execute(query)
        result = cursor.fetchall()
        result = json.loads(json.dumps(result, default=json_serializer))
        return result
