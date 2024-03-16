from datetime import datetime
from typing import List

from pydantic import BaseModel


class Url(BaseModel):
    id: int = None
    address: str = None


class Spider(BaseModel):
    id: int = None  # in pydantic 2 we must use None as default
    code: str = None
    name: str = None
    tag: str = None
    urls: List[Url] = None

