# WebService - Integração Corporativa com FastAPI

WebService desenvolvido com FastAPI para integração entre ambientes corporativos, automatizando processos de geração de relatórios e cargas de dados via API.

O projeto foi estruturado seguindo boas práticas do ecossistema FastAPI, utilizando separação por camadas, organização modular e configuração baseada em ambiente.

---

# Objetivo

O WebService atua como uma camada intermediária responsável por:

- Receber requisições JSON vindas de sistemas internos;
- Executar consultas em banco de dados;
- Processar e transformar os dados;
- Gerar novos payloads JSON;
- Integrar com outros ambientes e sistemas corporativos via API.

---

# Funcionalidades

## Relatórios

O módulo de relatórios recebe um JSON contendo parâmetros e queries utilizadas para coleta de dados em banco.

Após o processamento:

1. Os dados são consultados;
2. Um novo JSON estruturado é gerado;
3. Esse payload é enviado para um ambiente isolado responsável pela geração de relatórios.

### Fluxo

```text
Sistema Interno
    ↓
WebService FastAPI
    ↓
Banco de Dados
    ↓
Transformação dos Dados
    ↓
Ambiente Gerador de Relatórios
````

---

## Carga de Dados

O módulo de carga segue um fluxo semelhante ao módulo de relatórios.

Após a geração do JSON:

1. Os dados são processados;
2. O payload é estruturado;
3. O WebService realiza integrações via API para efetuar cargas em sistemas corporativos.

### Fluxo

```text
Sistema Interno
    ↓
WebService FastAPI
    ↓
Banco de Dados
    ↓
Transformação dos Dados
    ↓
API do Sistema de Destino
```

---

# Estrutura do Projeto

A estrutura foi organizada seguindo padrões recomendados pelo FastAPI para facilitar manutenção, escalabilidade e separação de responsabilidades.

```bash
app/
├── api/
│   ├── routes/
│   │   ├── reports.py
│   │   └── loads.py
│   └── dependencies.py
│
├── core/
│   ├── config.py
│   ├── security.py
│   └── database.py
│
├── schemas/
│   ├── report_schema.py
│   └── load_schema.py
│
├── services/
│   ├── report_service.py
│   └── load_service.py
│
├── integrations/
│   ├── report_api.py
│   └── external_system_api.py
│
├── utils/
│   ├── logger.py
│   └── helpers.py
│
├── main.py
└── __init__.py
```

---

# Tecnologias Utilizadas

* FastAPI
* Python
* Uvicorn
* Pydantic
* Requests / HTTPX
* SQLAlchemy
* PostgreSQL / Oracle / SQL Server

---

# Exemplo de Requisição

## Endpoint - Relatórios

```http
POST /reports/generate
```

### Body

```json
{
  "report_name": "sales_report",
  "queries": [
    {
      "name": "sales",
      "query": "SELECT * FROM sales WHERE date >= CURRENT_DATE"
    }
  ],
  "parameters": {
    "company": "COMPANY_A",
    "environment": "production"
  }
}
```

---

## Endpoint - Carga

```http
POST /loads/execute
```

### Body

```json
{
  "integration": "customer_sync",
  "queries": [
    {
      "name": "customers",
      "query": "SELECT * FROM customers WHERE active = 1"
    }
  ],
  "destination": {
    "system": "ERP",
    "module": "customers"
  }
}
```

---

# Padrões Utilizados

* Arquitetura modular
* Separação por camadas
* Uso de Schemas com Pydantic
* Configuração via `.env`
* Serviços desacoplados
* Integrações isoladas
* Reutilização de código
* Tipagem com Python
* Estrutura preparada para escalabilidade

---

# Segurança

As credenciais de banco de dados e APIs externas são armazenadas em variáveis de ambiente através de arquivo `.env`.

Por segurança, o arquivo `.env` não é versionado no repositório.

---

# Instalação

As instruções completas de instalação e configuração estão disponíveis em:

```text
INSTALL.md
```

---

# Melhorias Futuras

* Sistema de filas
* Retry automático
* Logs centralizados
* Observabilidade
* Cache de consultas
* Autenticação JWT
* Documentação OpenAPI customizada
* Testes automatizados

---

# Autor

Desenvolvido para uso interno corporativo utilizando FastAPI como framework principal.
