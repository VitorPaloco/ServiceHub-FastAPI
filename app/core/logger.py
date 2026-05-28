import logging
from datetime import datetime
from zoneinfo import ZoneInfo
from contextvars import ContextVar

log_file = "../app.log"

request_id_var = ContextVar("request_id", default=0)

class CustomFormatter(logging.Formatter):
    def format(self, record):
        record.request_id = request_id_var.get()
        return super().format(record)

logger = logging.getLogger("app")

formatter = CustomFormatter('[%(asctime)s] [%(request_id)s] %(levelname)s: %(message)s', '%Y-%m-%d %H:%M:%S')
formatter.converter = lambda ts: datetime.fromtimestamp(ts, ZoneInfo('America/Sao_Paulo')).timetuple()

handler = logging.FileHandler(log_file)
handler.setFormatter(formatter)

logger.handlers = [handler]
logger.setLevel(logging.INFO)
logger.propagate = False