from pydantic import BaseModel, model_validator, field_serializer
from pydantic_extra_types.color import Color

from .utils import convert_color_to_hex


class Moodlight(BaseModel):
    """Moodlight
    :param brightness: matrix custom brightness
    :param kelvin: matrix custom temperature
    :param color: matrix custom color
    """

    brightness: int = None
    kelvin: int = None
    color: Color = None

    @model_validator(mode="after")
    def check_constraint_blink_text(self) -> "Moodlight":
        if self.kelvin and self.color:
            raise ValueError("kelvin and color can't be set together")
        return self

    @field_serializer("color")
    def convert_color_to_hex(v: Color) -> str:
        if v:
            return convert_color_to_hex(v)
        return v
