from pydantic import BaseModel
from typing import Optional

class Query(BaseModel):
    db: str
    query: str

class Carga(BaseModel):
    id_api: str
    metodo_api: str
    caminho_api: str
    query_header: Query
    query_line1: Optional[Query] = None
    query_line2: Optional[Query] = None
    query_line3: Optional[Query] = None
    query_line4: Optional[Query] = None
    query_line5: Optional[Query] = None