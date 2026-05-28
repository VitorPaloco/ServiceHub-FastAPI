import os
import json
import requests
from dotenv import load_dotenv

# Gerar arquivo via Carbone
def carbone_render(body):
    load_dotenv()

    base_url = os.getenv('API_001_BASE_URL')
    headers = json.loads(os.getenv('API_001_HEADERS'))
    req_url = os.path.join(base_url, 'render')

    return requests.post(req_url, headers=headers, json=body)


def login(id_env):
    try:
        load_dotenv()

        auth_type = os.getenv(f'API_{id_env}_AUTH_TYPE')
        base_url = os.getenv(f'API_{id_env}_BASE_URL')

        headers = json.loads(os.getenv(f'API_{id_env}_HEADERS'))

        if auth_type == 'login':
            login_url = base_url.rstrip("/") + "/" + os.getenv(f'API_{id_env}_AUTH_URL')
            login_method = os.getenv(f'API_{id_env}_AUTH_METHOD')
            login_body = json.loads(os.getenv(f'API_{id_env}_AUTH_BODY'))
            token_path = os.getenv(f'API_{id_env}_TOKEN_PATH')

            login_req = requests.request(login_method, login_url, json=login_body, timeout=60)
            token = login_req.json().get(token_path)

            headers['Authorization'] = f'Bearer {token}'

        return base_url, headers
    
    except Exception as e:
        raise Exception(f'Erro ao realizar autenticação: {e}')
    

# CARGA ITERATIVA
def carga_api(body, req_url, metodo, headers):
    return requests.request(metodo, req_url, json=body, headers=headers, timeout=60)