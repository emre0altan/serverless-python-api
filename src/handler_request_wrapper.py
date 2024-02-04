from dynamodb_json import json_util as json

def get_item_wrapper(table, query, identifier):
    try:
        print(f'Identifier: {identifier}')
        print(table)
        print("\tHost: " + table.meta.client._endpoint.host)
        response = table.get_item(Key=query)
        result = json.loads(json.dumps(response))
        print("Result:\n\t" + str(result))
        if 'Item' in result:
            item = result['Item']
            return (True, item)
        elif 'ResponseMetadata' in result and result['ResponseMetadata']['HTTPStatusCode'] == 200:
                return (False, result)
        return (False, result)
    except Exception as e:
        return (False, {'error': e})

def delete_item_wrapper(table, query, identifier):
    print(f'Identifier: {identifier}')
    response = table.delete_item(Key=query)
    result = json.loads(json.dumps(response))
    print("\tHost: " + table.meta.client._endpoint.host)
    print("Result:\n\t" + str(result))
    if 'ResponseMetadata' in result and result['ResponseMetadata']['HTTPStatusCode'] == 200:
            return (True, result)
    return (False, result)

def put_item_wrapper(table, item, identifier):
    print(f'Identifier: {identifier}')
    response = table.put_item(Item=item)
    result = json.loads(json.dumps(response))
    print("\tHost: " + table.meta.client._endpoint.host)
    print("Result:\n\t" + str(result))
    if 'ResponseMetadata' in response and response['ResponseMetadata']['HTTPStatusCode'] == 200:
            return (True, response)
    return (False, response)

def update_item_wrapper(table, key, upExp, expAttr, expAttrName, identifier):
    print(f'Identifier: {identifier}')
    response = table.update_item(Key=key, UpdateExpression=upExp, ExpressionAttributeValues=expAttr, ExpressionAttributeNames=expAttrName)
    result = json.loads(json.dumps(response))
    print("\tHost: " + table.meta.client._endpoint.host)
    print("Result:\n\t" + str(result))
    if 'ResponseMetadata' in response and response['ResponseMetadata']['HTTPStatusCode'] == 200:
            return (True, response)
    return (False, response)

def scan_table_wrapper(table, id_for_sort, identifier):
    print(f'Identifier: {identifier}')
    response = table.scan()
    result = json.loads(json.dumps(response))
    print("\tHost: " + table.meta.client._endpoint.host)
    print("Result:\n\t" + str(result))
    if 'Items' in result:
        items = result['Items']
        if len(items) > 0:
            sorted_items = sorted(items, key=lambda x : x[id_for_sort])
            return (True, sorted_items)
        else:
            return (False, {'error': 'No item found!'})
    elif 'ResponseMetadata' in result and result['ResponseMetadata']['HTTPStatusCode'] == 200:
            return (True, result)
    return (False, result)

def query_table_wrapper(table, kCExpression, id_for_sort, identifier):
    print(f'Identifier: {identifier}')
    response = table.query(KeyConditionExpression=kCExpression)
    result = json.loads(json.dumps(response))
    print("\tHost: " + table.meta.client._endpoint.host)
    print("Result:\n\t" + str(result))
    if 'Items' in result:
        items = result['Items']
        if len(items) > 0:
            sorted_items = sorted(items, key=lambda x : x[id_for_sort])
            return (True, sorted_items)
        else:
            return (False, result)
    elif 'ResponseMetadata' in result and result['ResponseMetadata']['HTTPStatusCode'] == 200:
            return (True, result)
    return (False, result)