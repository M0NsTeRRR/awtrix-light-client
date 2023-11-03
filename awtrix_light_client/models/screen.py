from typing import List
from pydantic import BaseModel, Field


class Screen(BaseModel):
    matrix: List[int] = Field(min_length=256, max_length=256)
