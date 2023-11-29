from os import environ
from aiohttp.web import run_app
from aiohttp.web_app import Application
from aiohttp.web_request import Request
from aiohttp.web_response import Response
from walletpay.types.update import Update

app = Application()