from typing import List
from pydantic import BaseModel


class Loop(BaseModel):
    """Loop
    :param loops: List of all apps in the loop
    """

    loops: List[str]
