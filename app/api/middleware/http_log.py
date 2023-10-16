from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
import logging


logger = logging.getLogger("api")


class HttpLog(BaseHTTPMiddleware):
    """This middleware log when HTTP request is received and responded"""

    def __init__(self, app):
        super().__init__(app)

    async def dispatch(self, request: Request, call_next):
        # log the start of processing the request
        header = f"{request.method} {request.url.path}"
        logger.info(f"{header} processing...")

        # process the request
        response = await call_next(request)

        # log the end of processing the request
        logger.info(f"{header} done.")

        return response
