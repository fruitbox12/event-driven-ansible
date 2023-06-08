import sys
from os import environ

from aiohttp import web
from aiohttp.web_request import Request
from aiohttp.web_response import Response

routes = web.RouteTableDef()


@routes.get("/health")
async def health(request: Request) -> Response:
    return web.json_response({"status": "RUNNING"})


@routes.get("/down")
async def down(request: Request) -> Response:
    # simulate program crashing
    sys.exit(1)


@routes.get("/status")
async def health(request: Request) -> Response:
    return web.json_response({"status": "COMPLETED"})

if __name__ == "__main__":
    app = web.Application()
    app.add_routes(routes)
    port = int(environ.get("HTTP_PORT", 5080))
    web.run_app(app=app, port=port)
