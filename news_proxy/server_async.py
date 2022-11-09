import aiohttp
from aiohttp import web
from bs4 import BeautifulSoup

# https://pypi.org/project/aiohttp-client-cache/
# leave only one route

BASE_URL = "https://news.ycombinator.com"
DEFAULT_PORT = 8232


def modify_html(html):
    soup = BeautifulSoup(html, "html.parser")

    title = soup.find("title")
    if title:
        title.string = "Custom Title"

    return soup.prettify()


def modify_text(text):
    return text


async def handle(request):

    page_url = BASE_URL + request.path_qs
    page_html = await download_page(page_url)
    new_html = modify_html(page_html)
    return web.Response(text=new_html, content_type="text/html")


async def download_page(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            html = await resp.text()
            return html


if __name__ == "__main__":
    app = web.Application()
    app.add_routes([web.get("/", handle), web.get("/{qs}", handle)])
    web.run_app(app, port=DEFAULT_PORT)
