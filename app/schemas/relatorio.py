from pydantic import BaseModel
from typing import Optional

class Query(BaseModel):
    db: str
    query: str

class Relatorio(BaseModel):
    template_path: str
    extensao_relatorio: str
    output_path: str
    query_header: Query
    query_line1: Optional[Query] = None
    query_line2: Optional[Query] = None
    query_line3: Optional[Query] = None
    query_line4: Optional[Query] = None
    query_line5: Optional[Query] = None