import requests

def test_calc():
    req = requests.get('http://localhost:8080/get?speech=123加456')
    text = req.json()
    print(text)
    assert text['text'] == '123 + 123 = 246'
