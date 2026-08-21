import importlib
import logging

from fastapi import FastAPI, Request

from app.controllers import pages

logger = logging.getLogger('app')


def create_app(config_filename):
    config = importlib.import_module(config_filename)
    app = FastAPI(debug=getattr(config, 'DEBUG', False))

    app.include_router(pages.router)

    logger.setLevel(logging.NOTSET)

    @app.middleware('http')
    async def log_response(request: Request, call_next):
        response = await call_next(request)
        body = await request.body()
        logger.info(
            "{} {} {}\n{}".format(request.method, request.url, body, response)
        )
        return response

    return app
