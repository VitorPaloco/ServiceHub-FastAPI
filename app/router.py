from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from schemas.relatorio import Relatorio
from schemas.carga import Carga
from core.config import auth_token
from core.logger import logger
from services import query_service, api_service

router = APIRouter()

@router.post("/relatorio/carbone")
def relatorio_carbone(payload: Relatorio, token: str = Depends(auth_token)):
    try:    
        logger.info('Realizando queries...')
        dados_query = query_service.processar_queries(payload)

        if not dados_query:
            logger.error('Nenhum resultado encontrado')
            return JSONResponse(content={'Erro': 'Nenhum resultado encontrado'}, status_code=500)

        logger.info('Gerando arquivo no Carbone...')

        carbone_body = {
            'template_path': payload.get('template_path'),
            'extensao_relatorio': payload.get('extensao_relatorio'),
            'output_path': payload.get('output_path'),
            'dados_query': dados_query
        }

        carbone_req = api_service.carbone_render(carbone_body)

        if carbone_req.status_code != 200:
            logger.error(carbone_req.json().get('error'))
            return JSONResponse(content=carbone_req.json(), status_code=500)

        logger.info(f'Arquivo: {carbone_req.json().get('file_url')}')
        return JSONResponse(content=carbone_req.json().get('file_url'), status_code=200)
    
    except Exception as e:
        logger.error(str(e))
        return JSONResponse(content={'Erro': str(e)}, status_code=500)
    

@router.post("/carga")
def carga(payload: Carga, token: str = Depends(auth_token)):
    try:
        logger.info('Realizando queries...')
        dados_query = query_service.processar_queries(payload)

        if not dados_query:
            logger.error('Nenhum resultado encontrado')
            return JSONResponse(content={'Erro': 'Nenhum resultado encontrado'}, status_code=500)
        
        logger.info(f'Query realizada, {len(dados_query)} itens encontrados')

        # AUTENTICAÇÃO DA CARGA

        id_api = payload.get('id_api')
        base_url, headers = api_service.login(id_api)
        
        caminho_api = payload.get('caminho_api')
        metodo_api = payload.get('metodo_api')
        carga_url = base_url.rstrip('/') + '/' + caminho_api

        erros_carga = 0

        # ITERAÇÃO DA CARGA

        for carga in dados_query:
            try:
                carga_req = api_service.carga_api(carga, carga_url, metodo_api, headers)
                carga_req.raise_for_status()

                logger.info(f'Carga realizada com sucesso!')

            except Exception as e:
                erros_carga += 1       
                logger.error(f'Erro na carga: {e} | {carga_req.text }')

                continue

        logger.info(f'Finalizando Carga, {erros_carga} erros encontrados')
        return JSONResponse(content={'Carga finalizada': f'{erros_carga} erros encontrados'}, status_code=200)
        
    except Exception as e:
        logger.error(str(e))
        return JSONResponse(content={'Erro': str(e)}, status_code=500)
    
