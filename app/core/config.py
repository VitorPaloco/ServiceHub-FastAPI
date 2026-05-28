from fastapi import HTTPException, Depends, Request
from fastapi.responses import JSONResponse
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from dotenv import load_dotenv
import random
import time
import os
from core.logger import logger, request_id_var

security = HTTPBearer(auto_error=False)

load_dotenv()
TOKEN_AUTORIZADO = os.getenv("AUTHORIZED_TOKEN")

async def auth_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    if credentials is None:
        logger.error("Token ausente")
        raise HTTPException(status_code=401, detail="Token ausente")

    token = credentials.credentials

    if token != TOKEN_AUTORIZADO:
        logger.error("Token inválido")
        raise HTTPException(status_code=401, detail="Token inválido")
    
    return token


def middleware(app):
    @app.middleware('http')
    async def request_middleware(request: Request, call_next):
        cod_tempo = str(int(time.time()))[-4:]
        cod_random = str(random.randint(100,999))

        request_id = int(cod_tempo + cod_random)
        request_id_var.set(request_id)

        logger.info(f'Requisição iniciada | IP: {request.client.host} | Path: {request.url.path}')
        return await call_next(request)

    @app.exception_handler(404)
    async def fallback(request: Request, exc):
        logger.error('Rota não encontrada')
        return JSONResponse(content={'Erro': 'Rota não encontrada'}, status_code=404)