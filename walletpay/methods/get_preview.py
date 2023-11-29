from typing import Any
from .base import Method
from dataclasses import dataclass
from ..types.get_preview_response import GetPreviewResponse

@dataclass
class GetPreviewRequest(Method[GetPreviewResponse]):
  __returning__ = GetPreviewResponse
  __api_method__ = "order/preview"
  __http_method__ = "get"
  id: str

  def query_parms(self) -> dict[str, Any]:
    return {"id": self.id}
  
  def to_json(self) -> dict[str, Any] | None:
    return None