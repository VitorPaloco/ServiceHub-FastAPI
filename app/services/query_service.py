from datetime import datetime, date
from dotenv import load_dotenv
from decimal import Decimal
import psycopg2, pymssql
from hdbcli import dbapi
import os


# Tratamento do JSON
def formatar_json(obj):
    if isinstance(obj, (datetime, date)): # Formatação de datas
        return obj.strftime('%Y-%m-%d')

    if isinstance(obj, Decimal): # Formatação de decimais
        return float(obj)

    if isinstance(obj, dict): # Remoção de itens vazios
        novo = {}
        for k, v in obj.items():
            v_tratado = formatar_json(v)
            if v_tratado not in ({}, [], None):
                novo[k] = v_tratado
        return novo

    if isinstance(obj, list): # Remoção de listas vazias
        nova = []
        for item in obj:
            item_tratado = formatar_json(item)
            if item_tratado not in ({}, [], None):
                nova.append(item_tratado)
        return nova

    return obj


# Conexão com o Banco de Dados
def conexao_bancodados(id):
    load_dotenv()

    db_tipo = os.getenv(f"DB_{id}_TYPE")
    db_host = os.getenv(f"DB_{id}_HOST")
    db_port = os.getenv(f"DB_{id}_PORT")
    db_database = os.getenv(f"DB_{id}_DATABASE")
    db_user = os.getenv(f"DB_{id}_USER")
    db_password = os.getenv(f"DB_{id}_PASSWORD")

    match db_tipo:
        case "hana":
            return dbapi.connect(address=db_host, port=db_port, user=db_user, password=db_password)
        case "postgres":
            return psycopg2.connect(host=db_host, port=db_port, database=db_database, user=db_user, password=db_password)
        case "sql_server":
            return pymssql.connect(server=db_host, database=db_database, user=db_user, password=db_password)
        case _:
            raise ValueError("Banco não identificado")


# Substituir Filtros - Exemplo: [%HeaderID]
def substituir_placeholders(query, parametros):
    for param, valor in parametros.items():
        if isinstance(valor, str):
            valor = valor.replace("'", "''")
            valor = f"'{valor}'"

        query = query.replace(f'[%{param}]', str(valor))

    return query


# Executar uma Query
def executar_sql(query_info, parametros):
    try:
        db_id = query_info.get("db")
        db_query = substituir_placeholders(query_info.get("query"), parametros)

        conn = conexao_bancodados(db_id)
        cursor = conn.cursor()
        cursor.execute(db_query)
        
        columns = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()
        
        cursor.close()

        return [formatar_json(dict(zip(columns, row))) for row in rows]
    
    except Exception as e:
        raise ValueError(f"Erro ao executar query: {e}")
    

# Processar Queries recurssivamente
def processar_queries(data, nome="query_header", parametros=None, caminho=None):
    if parametros is None:
        parametros = {}
    
    if caminho is None:
        caminho = []

    caminho_atual = caminho + [nome]

    try:
        query = data.get(nome) # Obtém a query

        if not query:
            return None
        
        resultado = executar_sql(query, parametros) # Executa a query
        
        for linha in resultado: # Verifica se há subqueries para processar
            for chave, valor in linha.items():
                if isinstance(valor, str) and valor.startswith('query_line'):
                    subquery_params = {} # Prepara os parâmetros para a subquery
                    subquery_params.update(linha) # Adiciona todos os parâmetros do item atual
                    linha[chave] = processar_queries(data, valor, subquery_params, caminho_atual) # Processa a subquery recursivamente
        
        return resultado
    
    except Exception as e:
        if "Erro ao processar [" in str(e):
            raise e
        
        caminho_str = " > ".join(caminho_atual)
        raise ValueError(f"Erro ao processar [{caminho_str}]: {str(e)}") from e