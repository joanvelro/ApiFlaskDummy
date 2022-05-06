import requests

input_data = {"name": "Germany",
              "capital": "Berlin",
              "area": 357022}
url = 'http://127.0.0.1:5000/countries'

try:
    print('post')
    resp = requests.post(url=url,
                         headers={"Content-Type": "application/json"},
                         json=input_data)
    print(resp.content)
    print(resp.status_code)
    json_response = resp.json()
except Exception as err:
    print('(!) exception: {}'.format(err))

try:
    print('get')
    resp = requests.get(url=url)
    # print(resp.content)
    print(resp.status_code)
    json_response = resp.json()
    for item in json_response:
        print('{}'.format(item))
except Exception as err:
    print('(!) exception: {}'.format(err))


