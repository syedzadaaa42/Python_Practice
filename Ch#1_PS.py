import http.client 
import json 


#Q3

connection = http.client.HTTPSConnection("www.google.com")

connection.request("GET", "/todos/1")

response = connection.getresponse()

print("status:", response.status)
print("Reason:", response.reason)

data = response.read()

#Try decoding as a json:

try:
    json_data = json.loads(data)
    pretty_json = json.dumps(json_data, indent=4)
    print("Content", pretty_json)
except json.JSONDecodeError:
    print("Content", data.decode('utf-8'))
