import keyring
import requests
import json

def hashkey(datas):
    path = "uapi/hashkey"
    url = f"{url_base}/{path}"
    headers = {
        'content-Type': 'application/json',
        'appKey': app_key,
        'appSecret': app_secret,
    }
    res = requests.post(url, headers=headers, data=json.dumps(datas))
    hashkey = res.json()["HASH"]

    return hashkey

# 모의계좌
keyring.set_password('mock_app_key', '우승현', 'PSu1AptULxHnkykHNhcgeOvrgSxMBaoJSiGH')
keyring.set_password('mock_app_secret', '우승현', '14RPQBQHzSeKjbFb7IZ7h4lO/N6AhnQ4BVmqGVf2IfjAIHwErN8ew++ZLqu+T4T/G7MEraL0zaGD0GwflehBxkkHKZ6LSTLBfMu75cW4UbEaByegiYmfxWr7sxr8DGd1Bd5+Me3FDuCphYtrLlfPSoR6xjOh40ynhrTkjKOYpwVEYJTFyUM=')

# key
app_key = keyring.get_password('mock_app_key', '우승현')
app_secret = keyring.get_password('mock_app_secret', '우승현')

# base url
url_base = "https://openapivts.koreainvestment.com:29443" # 모의투자

# information
headers = {"content-type": "application/json"}
path = "oauth2/tokenP"
body = {
    "grant_type": "client_credentials",
    "appkey": app_key,
    "appsecret": app_secret
}

res = requests.post(f"{url_base}/{path}", headers=headers, data=json.dumps(body))
access_token = res.json()['access_token']

path = "uapi/domestic-stock/v1/quotations/inquire-price"
url = f"{url_base}/{path}"

headers = {
    "Content-Type": "application/json",
    "authorization": f"Bearer {access_token}",
    "appKey": app_key,
    "appSecret": app_secret,
    "tr_id": "FHKST01010100"
}

params = {"fid_cond_mrkt_div_code": "J", "fid_input_iscd": "005930"}

res = requests.get(url, headers=headers, params=params)
print(res.json()['output']['stck_prpr'])


# 매수 주문
path = "/uapi/domestic-stock/v1/trading/order-cash"
url = f"{url_base}/{path}"

data = {
    "CANO": "50095843",  # 계좌번호 앞 8지리
    "ACNT_PRDT_CD": "01",  # 계좌번호 뒤 2자리
    "PDNO": "005930",  # 종목코드
    "ORD_DVSN": "01",  # 주문 방법
    "ORD_QTY": "10",  # 주문 수량
    "ORD_UNPR": "0",  # 주문 단가 (시장가의 경우 0)
}

headers = {
    "Content-Type": "application/json",
    "authorization": f"Bearer {access_token}",
    "appKey": app_key,
    "appSecret": app_secret,
    "tr_id": "VTTC0802U",
    "custtype": "P",
    "hashkey": hashkey(data)
}

res = requests.post(url, headers=headers, data=json.dumps(data))
print(res.json())

path = "/uapi/domestic-stock/v1/trading/order-cash"
url = f"{url_base}/{path}"

data = {
    "CANO": "50095843",  # 계좌번호 앞 8지리
    "ACNT_PRDT_CD": "01",  # 계좌번호 뒤 2자리
    "PDNO": "005930",  # 종목코드
    "ORD_DVSN": "00",  # 주문 방법
    "ORD_QTY": "10",  # 주문 수량
    "ORD_UNPR": "50000",  # 주문 단가 (시장가의 경우 0)
}

headers = {
    "Content-Type": "application/json",
    "authorization": f"Bearer {access_token}",
    "appKey": app_key,
    "appSecret": app_secret,
    "tr_id": "VTTC0802U",
    "custtype": "P",
    "hashkey": hashkey(data)
}

res = requests.post(url, headers=headers, data=json.dumps(data))
print(res.json())
