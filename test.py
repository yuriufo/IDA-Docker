import base64
import requests

def predict():
    url = 'http://127.0.0.1:7777/execute_script'
    data = {'filename': 'test', 'timeout': '120'}
    response = requests.post(url, data=data, files={'file': open("bin.exe_", "rb")})

    data = base64.b64decode(response.json()['data'].encode())

    print(response.status_code, data)


if __name__ == '__main__':
    predict()
