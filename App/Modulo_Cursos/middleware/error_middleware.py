from starlette.middleware.base import BaseHTTPMiddleware
from fastapi.responses import JSONResponse


class ErrorMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request, call_next):

        try:

            response = await call_next(request)

            return response


        except Exception as e:

            return JSONResponse(
                status_code=500,
                content={
                    "success": False,
                    "mensaje": "Error interno del servidor",
                    "detalle": str(e)
                }
            )