from datetime import datetime
from typing import List

from pydantic import BaseModel


class Url(BaseModel):
    id: int = None
    address: str = None


class Spider(BaseModel):
    id: int = None
    code: str = None
    name: str = None
    tag: str = None
    urls: List[Url]

