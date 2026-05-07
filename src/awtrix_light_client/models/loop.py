from pydantic import BaseModel


class Loop(BaseModel):
    """Loop
    :param loops: List of all apps in the loop
    """

    loops: list[str]
