from typing import List, Literal

from pydantic_extra_types.color import Color


def convert_color_to_hex(color: Color) -> str:
    return as_hex(color, format="long").upper()


def convert_colors_to_hex(colors: List[Color]) -> str:
    return [convert_color_to_hex(color) for color in colors]


def as_hex(c: Color, format: Literal["short", "long"] = "short") -> str:
    """
    # https://github.com/pydantic/pydantic-extra-types/blob/main/pydantic_extra_types/color.py#L141
    Will be removed when pydantic-extra-type will release a new version
    """
    values = [round(c * 255) for c in c._rgba[:3]]
    if c._rgba.alpha is not None:
        values.append(round(c._rgba.alpha * 255))

    as_hex = "".join(f"{v:02x}" for v in values)
    if format == "short" and all(
        c in {int(c * 2, 16) for c in "0123456789abcdef"} for c in values
    ):
        as_hex = "".join(as_hex[c] for c in range(0, len(as_hex), 2))
    return "#" + as_hex
