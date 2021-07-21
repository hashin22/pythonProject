import requests
import json

# requets 모듈 사용 url에서 데이터 가져오기
url = requests.get("https://api.androidhive.info/contacts/")
# json 문자열
testData = url.text
print(testData)
print(type(testData)) #str(json 문자열)

# json 데이터 파싱.
data = json.loads(testData)
print(data)
print(type(data))

####################################
dic = data["contacts"][0]
print(dic['name'])
print(dic['email'])