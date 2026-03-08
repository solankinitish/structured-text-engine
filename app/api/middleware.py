import time
import uuid
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from app.utils.logger import get_logger

logger = get_logger(__name__)

class RequestLoggingMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next):

        request_id = str(uuid.uuid4())[:8]
        start_time = time.time()
        
        logger.info(f"[REQUEST] id={request_id} path={request.url.path} method={request.method}")

        response = await call_next(request)

        duration = (time.time() - start_time) * 1000

        logger.info(
            f"[RESPONSE] id={request_id} status={response.status_code} latency={duration:.2f}ms"
        )

        return response
