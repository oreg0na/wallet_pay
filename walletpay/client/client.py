from decimal import Decimal
from .session.base import BaseSession
# from .session._aiohttp import AiohttpSession
from ..methods import GetPreview, GetOrderAmount, Create, GetOrderList
from ..types import GetPreviewResponse, GetOrderAmountResponse, CreateResponse, MoneyAmount, CurrencyCode, OrderList

DEFAULT_TIMEOUT_SECONDS = 60