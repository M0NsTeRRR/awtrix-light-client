from pydantic_extra_types.color import Color


def convert_color_to_hex(color: Color) -> str:
    """Helper function to convert a color in hex format

    :param color: color to convert
    :return: color in hex format
    """
    return color.as_hex(format="long").upper()
