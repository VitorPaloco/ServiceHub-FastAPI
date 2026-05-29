# Instalação do WebService

Este documento descreve o processo de instalação e configuração do ambiente necessário para execução do WebService.

---

# Requisitos

- Python 3.11+
- Pip
- Virtualenv
- Banco de dados acessível
- Credenciais de APIs externas

---

# Clonando o Projeto

```bash
git clone <URL_DO_REPOSITORIO>

cd nome-do-projeto
````

---

# Criando Ambiente Virtual

Linux/macOS:

```bash
python -m venv .venv

source .venv/bin/activate
```

Windows:

```bash
python -m venv .venv

.venv\Scripts\activate
```

---

# Instalando Dependências

```bash
pip install -r requirements.txt
```

---

# Configuração do .env

O projeto utiliza um arquivo `.env` para armazenar credenciais e configurações do ambiente.

Crie um arquivo `.env` na raiz do projeto.

---

# Exemplo de .env

```env
# Ambiente
APP_NAME=integration_ws
APP_ENV=development
APP_PORT=8000

# Banco de Dados
DB_HOST=localhost
DB_PORT=5432
DB_NAME=database
DB_USER=user
DB_PASSWORD=password

# API Relatórios
REPORT_API_URL=https://api-report.company.com
REPORT_API_TOKEN=token_here

# API Sistemas Externos
LOAD_API_URL=https://api-load.company.com
LOAD_API_TOKEN=token_here
```

---

# Executando o Projeto

```bash
uvicorn app.main:app --reload
```

A aplicação ficará disponível em:

```text
http://localhost:8000
```

---

# Documentação Automática

FastAPI disponibiliza documentação automática nos endpoints:

## Swagger

```text
http://localhost:8000/docs
```

## ReDoc

```text
http://localhost:8000/redoc
```

---

# Estrutura Recomendada

```bash
project/
├── app/
├── requirements.txt
├── .env
├── .env.example
├── README.md
└── INSTALL.md
```

---

# Arquivo .env.example

Recomenda-se manter um arquivo `.env.example` no repositório contendo apenas a estrutura das variáveis utilizadas.

Exemplo:

```env
DB_HOST=
DB_PORT=
DB_NAME=
DB_USER=
DB_PASSWORD=

REPORT_API_URL=
REPORT_API_TOKEN=

LOAD_API_URL=
LOAD_API_TOKEN=
```

---

# Observações

* Nunca versionar o arquivo `.env`;
* Garantir acesso aos bancos e APIs utilizados;
* Validar conectividade antes de iniciar o serviço;
* Utilizar ambientes separados para desenvolvimento e produção.
