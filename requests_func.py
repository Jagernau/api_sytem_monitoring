import requests
import json

view = "getobjectslist"

#fort monitor
def login_frt(domain_name: str, login: str, password: str) -> str | None:
    """login in frt api get session_id"""
    url = f'https://{domain_name}/api/integration/v1/connect'
    params = {
            'login': login,
            'password': password,
            'lang': 'ru-ru',
            'timezone': '+3'
    }
    headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
    response = requests.get(url, params=params, headers=headers)
    if response.status_code == 200:
        return response.headers['SessionId']
    else:
        return None


def get_frt_json(token: str, domain_name: str, view: str):
    """get json from frt api"""
    url = f'https://{domain_name}/api/integration/v1/{view}'
    params = {
            'SessionId': str(token),
            'companyId': 0
    }
    headers = {'Content-type': 'application/json', 'Accept': 'application/json', "SessionId": token}
    response = requests.get(url, params=params, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None


#glonass monitor
def login_gln(domain_name: str, login: str, password: str) -> str | None:
    url = f'https://{domain_name}/api/v3/auth/login'
    data = {'login': login, 'password': password}
    headers = {'Content-type': 'application/json', 'accept': 'json'}
    response = requests.post(url, data=json.dumps(data), headers=headers)
    if response.status_code == 200:
        return response.json()["AuthId"]
    else:
        return None


def get_gln_json(token: str, domain_name: str, view: str):
    url = f"https://{domain_name}/api/{view}/"
    #url = f"https://{domain_name}/api/v3/devices/types"
    headers = {"X-Auth": token, 'Content-type': 'application/json', 'Accept': 'application/json'}
    response = requests.get(url, headers=headers,)
    if response.status_code == 200:
        result = response.json()
        return result
    else:
        return None

