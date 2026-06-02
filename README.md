## ⚙️ ServiceHub - Integração Corporativa com FastAPI
WebService desenvolvido com FastAPI para integração automatizar processos de geração de relatórios e cargas de dados via API.

O WebService atua como uma camada intermediária responsável por:

- Receber requisições JSON vindas de sistemas internos;
- Executar consultas em banco de dados;
- Processar e transformar os dados;
- Gerar novos payloads JSON;
- Integrar com outros ambientes e sistemas corporativos via API.

<br>

> O projeto foi estruturado seguindo boas práticas do ecossistema FastAPI, utilizando separação por camadas, organização modular e configuração baseada em ambiente.

<br>

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/> <img src="https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi&logoColor=white"/> 

## 📂 Project Structure

```bash
├── .venv/
├── app/
│   ├── core/
│   │   ├── config.py
│   │   └── logger.py
│   │
│   ├── schemas/
│   │   ├── carga.py
│   │   └── relatorio.py
│   │
│   ├── services/
│   │   ├── api_service.py
│   │   └── query_service.py
│   │
│   ├── main.py
│   └── router.py
├── logs/
└── .env
```

## 🔗 Instalação

Clone este repositório
```bash
git clone https://github.com/VitorPaloco/ServiceHub-FastAPI.git

cd ServiceHub-FastAPI
```

Crie seu ambiente virtual
```bash
# Linux / MacOS
python -m venv .venv
source .venv/bin/activate

# Windows
python -m venv .venv
.venv\Scripts\activate
```

Instalando dependências
```bash
pip install -r requirements.txt
```

Gere seu arquivo .env e preencha com os dados dos seus Bancos de Dados e APIs
```bash
cp .env.example .env
```

```env
# ==================================================
# APPLICATION
# ==================================================

# Internal application token
AUTHORIZED_TOKEN=your_authorized_token_here

# ==================================================
# DATABASE CONNECTIONS
# ==================================================
# Supported types:
# mysql | postgres | sqlserver | hana
# ==================================================

# DATABASE 001
DB_001_TYPE=
DB_001_HOST=
DB_001_PORT=
DB_001_DATABASE=
DB_001_USER=
DB_001_PASSWORD=

# ==================================================
# API INTEGRATIONS
# ==================================================
# AUTH TYPES:
# bearer -> Fixed bearer token
# login -> Authentication endpoint required
# ==================================================

# API 001 - Bearer Example
API_001_BASE_URL=http://localhost:8001/
API_001_HEADERS={"Authorization":"Bearer your_token_here","Content-Type":"application/json"}

# API 002 - Login Example
API_002_BASE_URL=
API_002_AUTH_TYPE=login
API_002_AUTH_URL=Login
API_002_AUTH_METHOD=POST
API_002_AUTH_BODY={}
API_002_TOKEN_PATH=SessionId
API_002_HEADERS={"Authorization":"","Content-Type":"application/json"}
```
