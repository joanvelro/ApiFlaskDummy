import requests

input_data = {"A": 23,
              "B": 45}

url = 'http://127.0.0.1:5000/calculation'


try:
    print('Calculate C = A^0.5 + B^2')
    print('Input:')
    for item, value in input_data.items():
        print('{}:{}'.format(item, value))
    resp = requests.post(url=url,
                         headers={"Content-Type": "application/json"},
                         json=input_data
                         )
    # print(resp.content)
    print('Status request:', resp.status_code)
    json_response = resp.json()
    print('Output')
    for item, value in json_response.items():
        print('{}:{}'.format(item, value))
except Exception as err:
    print('(!) exception: {}'.format(err))
