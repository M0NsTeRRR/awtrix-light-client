from typing import List
from pydantic import BaseModel


class Loop(BaseModel):
    loops: List[str]
