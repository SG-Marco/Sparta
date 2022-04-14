import requests # requests 라이브러리 설치 필요
import pprint


r = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
rjson = r.json()

# pprint.pprint(rjson['RealtimeCityAir'])


for i in rjson['RealtimeCityAir']['row']:
    if i['IDEX_MVL'] < 80 :
        print('구 이름 : ', i['MSRSTE_NM'], '//  미세먼지 수치 : ', i['IDEX_MVL'])


