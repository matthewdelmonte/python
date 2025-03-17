# Write to JSON in Python
import json


mydict = {
    "People": [
        {
            "name": "Matthew",
            "age": 53,
            "isStudent": True
        },
        {
            "name": "Kimberly",
            "age": 53,
            "isStudent": False
        },
        {
            "name": "Caleb",
            "age": 26,
            "isStudent": False
        },
        {
            "name": "Alyssa",
            "age": 24,
            "isStudent": True
        }
    ]
}

json_string = json.dumps(mydict, indent = 2)

with open('./Data/myjson_data', 'w') as f:
    f.write(json_string)