from typing import List, Union, Any, Optional
from enum import IntEnum

from pydantic import BaseModel, Field, model_validator, field_serializer
from pydantic.networks import Annotated, Url, UrlConstraints
from pydantic_extra_types.color import Color

from .effect import EffectType, EffectSetting
from .utils import convert_color_to_hex


class TextCase(IntEnum):
    GLOBAL = 0
    FORCE_UPPERCASE = 1
    SHOW_AS_IT_SEND = 2


class PushIcon(IntEnum):
    NOT_MOVING = 0
    MOVING_ONE_TIME = 1
    MOVING = 2


class Dp(BaseModel):
    x: int
    y: int
    cl: Color

    @field_serializer(
        "cl",
    )
    def convert_color_to_int(v: Color) -> str:
        if v:
            return convert_color_to_hex(v)
        else:
            return v


class Dl(BaseModel):
    x0: int
    y0: int
    x1: int
    y1: int
    cl: Color

    @field_serializer(
        "cl",
    )
    def convert_color_to_int(v: Color) -> str:
        if v:
            return convert_color_to_hex(v)
        else:
            return v


class Dr(BaseModel):
    x: int
    y: int
    w: int
    h: int
    cl: Color

    @field_serializer(
        "cl",
    )
    def convert_color_to_int(v: Color) -> str:
        if v:
            return convert_color_to_hex(v)
        else:
            return v


class Df(BaseModel):
    x: int
    y: int
    w: int
    h: int
    cl: Color

    @field_serializer(
        "cl",
    )
    def convert_color_to_int(v: Color) -> str:
        if v:
            return convert_color_to_hex(v)
        else:
            return v


class Dc(BaseModel):
    x: int
    y: int
    r: int
    cl: Color

    @field_serializer(
        "cl",
    )
    def convert_color_to_int(v: Color) -> str:
        if v:
            return convert_color_to_hex(v)
        else:
            return v


class Dfc(BaseModel):
    x: int
    y: int
    r: int
    cl: Color

    @field_serializer(
        "cl",
    )
    def convert_color_to_int(v: Color) -> str:
        if v:
            return convert_color_to_hex(v)
        else:
            return v


class Dt(BaseModel):
    x: int
    y: int
    t: int
    cl: Color

    @field_serializer(
        "cl",
    )
    def convert_color_to_int(v: Color) -> str:
        if v:
            return convert_color_to_hex(v)
        else:
            return v


class Db(BaseModel):
    x: int
    y: int
    r: int
    cl: Any

    # cl: Union[bytes, bytearray, memoryview] need to generate pydantic shema, leaving it for now
    @field_serializer(
        "cl",
    )
    def convert_color_to_int(v: Color) -> str:
        if v:
            return convert_color_to_hex(v)
        else:
            return v


class LifeTimeMode(IntEnum):
    DELETE = 0
    STALE = 1


class Fragment(BaseModel):
    t: str
    c: Color

    @field_serializer(
        "c",
    )
    def convert_color_to_int(v: Color) -> str:
        if v:
            return convert_color_to_hex(v)
        else:
            return v


class BaseApplication(BaseModel):
    text: Optional[Union[str, List[Fragment]]] = None
    textCase: Optional[TextCase] = None
    topText: Optional[bool] = None
    textOffset: Optional[int] = Field(default=None, ge=0)
    center: Optional[bool] = None
    color: Optional[Color] = None
    gradient: Optional[List[Color]] = Field(default=None, min_length=2, max_length=2)
    blinkText: Optional[int] = None
    fadeText: Optional[int] = None
    background: Optional[Color] = None
    rainbow: Optional[bool] = None
    icon: Optional[str] = None
    pushIcon: Optional[PushIcon] = None
    repeat: Optional[int] = Field(default=None, ge=-1)
    duration: Optional[int] = Field(default=None, ge=1)
    bar: Optional[List[int]] = Field(default=None, max_length=16)
    line: Optional[List[int]] = Field(default=None, max_length=16)
    autoscale: Optional[bool] = None
    progress: Optional[int] = Field(default=None, ge=-1, le=100)
    progressC: Optional[Color] = None
    progressBC: Optional[Color] = None
    draw: Optional[List[Union[Dp, Dl, Dr, Df, Dc, Dfc, Dt, Db]]] = None
    noScroll: Optional[bool] = None
    scrollSpeed: Optional[int] = Field(default=None, ge=0, le=100)
    effect: Optional[EffectType] = None
    effectSettings: Optional[EffectSetting] = None

    class ConfigDict:
        use_enum_values = True

    @model_validator(mode="after")
    def check_constraint_blink_text(self) -> "BaseApplication":
        if self.blinkText and (self.gradient or self.rainbow):
            raise ValueError(
                "blink text can be set only if gradient and rainbow are not used"
            )
        return self

    @model_validator(mode="after")
    def check_constraint_fade_text(self) -> "BaseApplication":
        if self.fadeText and (self.gradient or self.rainbow):
            raise ValueError(
                "fade text can be set only if gradient and rainbow are not used"
            )
        return self

    @model_validator(mode="after")
    def check_constraint_bar(self) -> "BaseApplication":
        if self.icon and self.bar and len(self.bar) > 11:
            raise ValueError("bar can have only 11 values with icon")
        return self

    @model_validator(mode="after")
    def check_constraint_line(self) -> "BaseApplication":
        if self.icon and self.line and len(self.line) > 11:
            raise ValueError("line can have only 11 values with icon")
        return self

    @field_serializer("color", "gradient", "background", "progressC", "progressBC")
    def convert_color_to_hex(v: Union[List[Color], Color]) -> Union[List, str]:
        if isinstance(v, List):
            return [convert_color_to_hex(color) for color in v]
        else:
            return convert_color_to_hex(v)


class CustomApplication(BaseApplication):
    pos: Optional[int] = Field(default=None, ge=0)
    lifetime: Optional[int] = Field(default=None, ge=0)
    lifetimeMode: Optional[LifeTimeMode] = None
    save: Optional[bool] = None


CLIENT_TYPE = Annotated[
    Url, UrlConstraints(allowed_schemes=["http", "https", "mqtt", "mqtts"])
]


class Notification(BaseApplication):
    hold: Optional[bool] = None
    sound: Optional[str] = None
    rtttl: Optional[str] = None
    loopSound: Optional[bool] = None
    stack: Optional[bool] = None
    wakeup: Optional[bool] = None
    clients: Optional[List[CLIENT_TYPE]] = None

    @model_validator(mode="after")
    def check_constraint_sound_rtttl(self) -> "Notification":
        if self.sound and self.rtttl:
            raise ValueError("sound and rtttl can't be set together")
        return self

    @field_serializer("clients")
    def convert_url_to_str(clients: CLIENT_TYPE) -> List[str]:
        return [str(client) for client in clients]
