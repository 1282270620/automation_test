import requests

def headers():      #post登陆p2p
    urll="http://192.168.0.105/Logo/logings.html" 
    headers ={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
              }
    data = {'username':'admin','password':'123456'}
    response=requests.post(url=urll, data=data, json=headers)

    print(response.text)
    #print(response.read().decode('utf-8'))

headers()
