import requests
import json

url = requests.get("https://api.androidhive.info/contacts/")
# json 문자열
testData = url.text
print(testData)
print(type(testData)) #str(json 문자열)

data = json.loads(testData)
print(data)
print(type(data))

####################################
dic = data["contacts"][0]
print(dic['name'])
print(dic['email'])