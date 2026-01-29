from typing import List, Union, Optional
from enum import IntEnum

from pydantic import BaseModel, Field, model_validator, field_serializer
from pydantic.networks import Annotated, UrlConstraints
from pydantic_core import Url
from pydantic_extra_types.color import Color

from .effect import EffectType, EffectSetting
from .utils import convert_color_to_hex


class TextCase(IntEnum):
    GLOBAL = 0
    """
    """

    FORCE_UPPERCASE = 1
    """
    """

    SHOW_AS_IT_SEND = 2
    """
    """


class PushIcon(IntEnum):
    NOT_MOVING = 0
    """
    """

    MOVING_ONE_TIME = 1
    """
    """

    MOVING = 2
    """
    """


class Dp(BaseModel):
    """Draw a pixel
    :param x: Pixel x axis
    :param y: Pixel y axis
    :param cl: Pixel color
    """

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
    """Draw a line
    :param x0: Start pixel x axis
    :param y0: Start pixel y axis
    :param x1: End pixel x axis
    :param y1: End pixel y axis
    :param cl: Line color
    """

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
    """Draw a rectangle
    :param x: Top left corner pixel x axis
    :param y: Top left corner pixel y axis
    :param w: Width
    :param h: High
    :param cl: Line color
    """

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
    """Draw a filled rectangle
    :param x: Top left corner pixel x axis
    :param y: Top left corner pixel y axis
    :param w: Width
    :param h: High
    :param cl: Line color
    """

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
    """Draw a circle
    :param x: Circle center x axis
    :param y: Circle center y axis
    :param r: Radius
    :param cl: Line color
    """

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
    """Draw a filled circle
    :param x: Circle center x axis
    :param y: Circle center y axis
    :param r: Radius
    :param cl: Line color
    """

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
    """Draw text
    :param x: Text top left corner pixel x axis
    :param y: Text top left corner pixel y axis
    :param t: Text
    :param cl: Line color
    """

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
    """Draws a RGB888 bitmap array
    :param x: Top left corner pixel x axis
    :param y: Top left corner pixel y axis
    :param w: Width
    :param h: High
    :param bmp: Bitmap array
    """

    x: int
    y: int
    w: int
    h: int
    bmp: List[str]

    # bmp: Union[bytes, bytearray, memoryview] need to generate pydantic schema, leaving it for now


class LifeTimeMode(IntEnum):
    DELETE = 0
    """
    """

    STALE = 1
    """
    """


class Fragment(BaseModel):
    """A fragment of text
    :param t: Text
    :param c: Color
    """

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
    """Base application class

    :param text: The text to display. Keep in mind the font does not have a fixed size and I uses less space than W. This facts affects when text will start scrolling
    :param textCase: Changes the Uppercase setting.
    :param topText: Draw the text on top.
    :param textOffset: Sets an offset for the x position of a starting text.
    :param center: Centers a short, non-scrollable text.
    :param color: The text, bar or line color.
    :param gradient: Colorizes the text in a gradient of two given colors.
    :param blinkText: Blinks the text in an given interval, not compatible with gradient or rainbow.
    :param fadeText: Fades the text on and off in an given interval, not compatible with gradient or rainbow.
    :param background: Sets a background color.
    :param rainbow: Fades each letter in the text differently through the entire RGB spectrum.
    :param icon: The icon ID or filename (without extension) to display on the app. You can also send a 8x8 jpg as Base64 String
    :param pushIcon: Icon movement.
    :param repeat: Sets how many times the text should be scrolled through the matrix before the app ends.
    :param duration: Sets how long the app or notification should be displayed.
    :param bar: Draws a bargraph. Without icon maximum 16 values, with icon 11 values.
    :param line: Draws a linechart. Without icon maximum 16 values, with icon 11 values.
    :param autoscale: Enables or disables autoscaling for bar and linechart.
    :param progress: Shows a progress bar. Value can be 0-100.
    :param progressC: The color of the progress bar.
    :param progressBC: The color of the progress bar background.
    :param draw: Array of drawing instructions. Each object represents a drawing command. See the drawing instructions below.
    :param noScroll: Disables the text scrolling.
    :param scrollSpeed: Modifies the scroll speed. Enter a percentage value of the original scroll speed.
    :param effect: Shows an effect as background.The effect can be removed by sending an empty string for effect.
    :param effectSettings: Changes color and speed of the effect.
    """

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
    """Custom application

    :param pos: Defines the position of your custom page in the loop, starting at 0 for the first position. This will only apply with your first push. This function is experimental.
    :param lifetime: Removes the custom app when there is no update after the given time in seconds.
    :param lifetimeMode: 0 = deletes the app, 1 = marks it as staled with a red rectangle around the app
    :param save: Saves your custom app into flash and reloads it after boot. Avoid this for custom apps with high update frequencies because the ESP's flash memory has limited write cycles.
    """

    pos: Optional[int] = Field(default=None, ge=0)
    lifetime: Optional[int] = Field(default=None, ge=0)
    lifetimeMode: Optional[LifeTimeMode] = None
    save: Optional[bool] = None


CLIENT_TYPE = Annotated[
    Url, UrlConstraints(allowed_schemes=["http", "https", "mqtt", "mqtts"])
]


class Notification(BaseApplication):
    """Notification

    :param hold: Set it to true, to hold your notification on top until you press the middle button or dismiss it via HomeAssistant. This key only belongs to notification.
    :param sound: The filename of your RTTTL ringtone file placed in the MELODIES folder (without extension).
    :param rtttl: Allows to send the RTTTL sound string with the json.
    :param loopSound: Loops the sound or rtttl as long as the notification is running.
    :param stack: Defines if the notification will be stacked. false will immediately replace the current notification.
    :param wakeup: If the Matrix is off, the notification will wake it up for the time of the notification.
    :param clients: Allows forwarding a notification to other awtrix devices. Use the MQTT prefix for MQTT and IP addresses for HTTP.
    """

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
