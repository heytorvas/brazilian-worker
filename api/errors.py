from exceptions import MaximumRawSalaryReachedException
from fastapi import Request
from fastapi.exceptions import HTTPException, RequestValidationError
from fastapi.responses import JSONResponse


def _parse_validation_error(exc):
    errors = exc.errors()
    return dict(
        content={
            'message': 'Validation error.',
            'errors': [
                {
                    'location': '.'.join([str(loc) for loc in error['loc']]),
                    'message': error['msg'],
                }
                for error in errors
            ],
        },
        status_code=400,
    )


def _generate_error(code, exc, internal=False):
    status_code = code // 100
    error_message = str(exc)

    return dict(
        content={
            'error': {
                'code': code,
                'message': 'Internal Server Error.' if internal else error_message,
            }
        },
        status_code=status_code,
    )


def error_handler(app):
    @app.exception_handler(RequestValidationError)
    async def validation_error_handler(request: Request, exc: RequestValidationError):
        return JSONResponse(**_parse_validation_error(exc))

    @app.exception_handler(HTTPException)
    async def http_exception_handler(request: Request, exc: HTTPException):
        return JSONResponse(**_generate_error(exc.status_code, exc.detail))

    @app.exception_handler(MaximumRawSalaryReachedException)
    async def maximum_raw_salary_reached_exception_handler(
        request: Request, exc: MaximumRawSalaryReachedException
    ):
        return JSONResponse(**_generate_error(42210, exc))

    @app.exception_handler(Exception)
    async def generic_error_handler(request: Request, exc: Exception):
        return JSONResponse(**_generate_error(50010, exc, internal=True))
