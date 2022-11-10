from aiohttp import web
from news_proxy.engine import handle, DEFAULT_PORT


def main() -> None:
    app = web.Application()
    app.add_routes([web.get("/{tail:.*}", handle)])
    web.run_app(app, port=DEFAULT_PORT)
