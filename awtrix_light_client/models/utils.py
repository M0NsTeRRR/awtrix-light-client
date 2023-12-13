from pydantic_extra_types.color import Color


def convert_color_to_hex(color: Color) -> str:
    return color.as_hex(format="long").upper()
