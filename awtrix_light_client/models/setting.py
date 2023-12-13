from typing import Any
from typing import Literal, Union

from pydantic_extra_types.color import Color
from pydantic import BaseModel, Field, field_validator, field_serializer

from .transition import TransitionType
from .utils import convert_color_to_hex


class Settings(BaseModel):
    ATIME: int = Field(default=None, ge=0)
    TEFF: TransitionType = None
    TSPEED: int = Field(default=None, ge=0)
    TCOL: Union[Color, int] = None
    TMODE: int = Field(default=None, ge=0, le=4)
    CHCOL: Union[Color, int] = None
    CBCOL: Union[Color, int] = None
    CTCOL: Union[Color, int] = None
    WD: bool = None
    WDCA: Union[Color, int] = None
    WDCI: Union[Color, int] = None
    BRI: int = Field(default=0, ge=0, le=255)
    ABRI: bool = None
    ATRANS: bool = None
    CCORRECTION: Union[Color, str] = None
    CTEMP: Union[Color, str] = None
    TFORMAT: Literal[
        "%H:%M:%S",
        "%l:%M:%S",
        "%H:%M",
        "%H %M",
        "%l:%M",
        "%l %M",
        "%l:%M %p",
        "%l %M %p",
    ] = None
    DFORMAT: Literal[
        "%d.%m.%y",
        "%d.%m",
        "%y-%m-%d",
        "%m-%d",
        "%m/%d/%y",
        "%m/%d",
        "%d/%m/%y",
        "%d/%m",
        "%m-%d-%y",
    ] = None
    SOM: bool = None
    CEL: bool = None
    MAT: int = None
    SOUND: bool = None
    GAMMA: float = None
    BLOCKN: bool = None
    UPPERCASE: bool = None
    TIME_COL: Union[Color, Literal[0]] = None
    DATE_COL: Union[Color, Literal[0]] = None
    TEMP_COL: Union[Color, Literal[0]] = None
    HUM_COL: Union[Color, Literal[0]] = None
    BAT_COL: Union[Color, Literal[0]] = None
    SSPEED: int = Field(default=None, ge=0, le=100)
    TIM: bool = None
    DAT: bool = None
    HUM: bool = None
    TEMP: bool = None
    BAT: bool = None
    MATP: bool = None

    class ConfigDict:
        use_enum_values = True

    @field_validator("CCORRECTION", "CTEMP", mode="before")
    @classmethod
    def convert_str_to_color(cls, v: Union[Color, str]) -> Color:
        if isinstance(v, str):
            return Color(v)
        else:
            return v

    @field_validator("TCOL", "CHCOL", "CBCOL", "CTCOL", "WDCA", "WDCI", mode="before")
    @classmethod
    def convert_integer_to_color(cls, v: Union[Color, int]) -> Color:
        if isinstance(v, int):
            return Color("{0:06X}".format(v))
        else:
            return v

    @field_serializer("CCORRECTION", "CTEMP")
    def convert_color_to_hex(v: Union[Color, str]) -> str:
        if isinstance(v, Color):
            return convert_color_to_hex(v)
        else:
            return v

    @field_serializer(
        "TCOL",
        "CHCOL",
        "CBCOL",
        "CTCOL",
        "WDCA",
        "WDCI",
        "TIME_COL",
        "DATE_COL",
        "TEMP_COL",
        "HUM_COL",
        "BAT_COL",
    )
    def convert_color_to_int(v: Any) -> int:
        if isinstance(v, Color):
            return int(v.as_hex(format="long")[1:], 16)
        else:
            return v
