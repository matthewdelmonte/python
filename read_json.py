import json

with open('./Data/myjson_data', 'r') as f:
    json_object = json.loads(f.read())

print(json_object['People'][0])