import requests,json

data = {'username':'Test Liu',
        'password':'123456'
}
res = requests.post(url='http://127.0.0.1:8080/login/', data=data)
print(res.text)
print(type(res.json()))