from fastapi import FastAPI
from app.api.routes import router
from app.api.error_handlers import invalid_input_handler
from app.exceptions import InvalidInputError
from app.api.middleware import RequestLoggingMiddleware

app = FastAPI(title="Structured Text Engine")

app.add_middleware(RequestLoggingMiddleware)

app.include_router(router)

app.add_exception_handler(InvalidInputError, invalid_input_handler)
