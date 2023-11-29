from __future__ import annotations
import abc
import json
import adaptix
from adaptix.load_error import LoadError
from typing import Callable, Any, Optional, Type, Final
from types import TracebackType
from ...exceptions import JsonDecodeError, ObjectLoadError, ServerError # корень WalletApi
from walletpay.methods.base import Method, ResponseType # methods

DEFAULT_TIMEOUT: float = 60.0

_JsonLoads = Callable[..., Any]

DEFAULT_HEADERS: Final[dict[str, str]] = {
    "Wpay-Store-Api-Key": ""
}

API_BASE_URL = "https://pay.wallet.tg/wpay/store-api/v1/{}"