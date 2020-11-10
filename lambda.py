def lambda_handler(event, context):
    output = []
    for record in event['records']:
        payload = base64.b64decode(record['data']).decode('utf-8')
        x = list(payload.split(","))
        result = str(model.predict([x])[0])
        output_record = {
            'recordId': record['recordId'],
            'result': 'Ok',
            'data': base64.b64encode(json.dumps(payload + ','+str(result)).encode('UTF-8')).decode()
            # 'data': base64.b64encode(json.dumps(str(result)).encode('UTF-8')).decode()
        }
        output.append(output_record)
    return {'records': output}
   
   
    # li = ''
    # for record in event['records']:
    #     payload = base64.b64decode(record['data']).decode('utf-8')
    #     x = list(payload.split(","))
    #     result = model.predict([x])
    #     li = li+','+str(result[0])
    # print(li)
    # return {
    #     'recordId': event['recordId'],
    #     'result':'Ok',
    #     'data' : base64.b64encode(json.dumps(li).encode('UTF-8')).decode()
    # }
   
    # li = list(event['record'].split("\n"))
    # fin = list()
    # for i in li:
    #     li2 = list(i.split(","))
    #     result = model.predict([li2])
    #     fin.append(result[0])
    #return fin
