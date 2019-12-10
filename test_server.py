import requests

def test_calc():
    req = requests.get('localhost:8080/get?speech=123加456')
    text = req.json()
    print(text)
    assert text['text'] == '123 + 456 = 579'

    req = requests.get('localhost:8080/get?speech=123加上456等於多少')
    assert text['text'] == '123 + 456 = 579'
