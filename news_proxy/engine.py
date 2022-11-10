from typing import Union

import aiohttp
import bs4
from aiohttp import web
from bs4 import BeautifulSoup

BASE_URL = "https://news.ycombinator.com"
DEFAULT_PORT = 8232


def modify_html(html: Union[str, bytes]) -> str:
    def tag_visible(element: bs4.element.PageElement) -> bool:
        if element.parent is not None and element.parent.name in [
            "style",
            "script",
            "head",
            "meta",
            "[document]",
        ]:
            return False
        return True

    soup = BeautifulSoup(html, "html.parser")

    for el in filter(tag_visible, soup.findAll(text=True)):
        el_string = el.string
        el.string.replace_with(modify_text(el_string))
    return soup.prettify()


def modify_text(text: str) -> str:
    words = text.split(" ")
    for k, word in enumerate(words):
        word_alpha = "".join(filter(str.isalpha, word))
        if len(word_alpha) == 6:
            words[k] = word.replace(word_alpha, word_alpha + "™")
    return " ".join(words)


async def handle(request: aiohttp.web_request.Request) -> aiohttp.web.Response:
    page_url = BASE_URL + request.path_qs
    page_html = await download_page(page_url)
    new_html = modify_html(page_html)
    return web.Response(text=new_html, content_type="text/html")


async def download_page(url: str) -> Union[str, bytes]:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            return await resp.content.read()
