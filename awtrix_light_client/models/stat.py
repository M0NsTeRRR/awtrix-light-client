from pydantic import BaseModel


class Stats(BaseModel):
    """Statistics

    :param bat: _description_
    """

    bat: int
    bat_raw: int
    type: int
    lux: int
    ldr_raw: int
    ram: int
    bri: int
    temp: int
    hum: int
    uptime: int
    wifi_signal: int
    messages: int
    version: str
    indicator1: bool
    indicator2: bool
    indicator3: bool
    app: str
    uid: str
    matrix: bool
