from typing import List
from pydantic import BaseModel, Field


class Screen(BaseModel):
    """Screen
    :param matrix: matrix screen as an array of 24bit colors
    """

    matrix: List[int] = Field(min_length=256, max_length=256)
