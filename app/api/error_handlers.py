from fastapi import Request
from fastapi.responses import JSONResponse
from app.exceptions import InvalidInputError


async def invalid_input_handler(request: Request, exc: InvalidInputError):
    return JSONResponse(
        status_code=400,
        content={"error": str(exc)}
    )
