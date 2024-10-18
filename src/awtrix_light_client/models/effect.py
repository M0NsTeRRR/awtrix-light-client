from pydantic import BaseModel
from enum import Enum


class Palette(str, Enum):
    CLOUD = "Cloud"
    """
    """

    LAVA = "Lava"
    """
    """

    OCEAN = "Ocean"
    """
    """

    FOREST = "Forest"
    """
    """

    STRIPE = "Stripe"
    """
    """

    PARTY = "Party"
    """
    """

    HEAT = "Heat"
    """
    """

    RAINBOW = "Rainbow"
    """
    """


class EffectType(str, Enum):
    FADE = "Fade"
    """
    """

    MOVINGLINE = "MovingLine"
    """
    """

    BRICKBREAKER = "BrickBreaker"
    """
    """

    PINGPONG = "PingPong"
    """
    """

    RADAR = "Radar"
    """
    """

    CHECKERBOARD = "Checkerboard"
    """
    """

    FIREWORKS = "Fireworks"
    """
    """

    PLASMACLOUD = "PlasmaCloud"
    """
    """

    RIPPLE = "Ripple"
    """
    """

    SNAKE = "Snake"
    """
    """

    PACIFICA = "Pacifica"
    """
    """

    THEATERCHASE = "TheaterChase"
    """
    """

    PLASMA = "Plasma"
    """
    """

    MATRIX = "Matrix"
    """
    """

    SWIRLIN = "SwirlIn"
    """
    """

    SWIRLOUT = "SwirlOut"
    """
    """

    LOOKINGEYES = "LookingEyes"
    """
    """

    TWINKLINGSTARS = "TwinklingStars"
    """
    """

    COLORWAVES = "ColorWaves"
    """
    """


class EffectSetting(BaseModel):
    """EffectSetting
    :param speed: Mostly 3 as standard. Higher means faster.
    :param palette: A color palette is an array of 16 colors to create transitions between colors.
    :param blend: Interpolates between colors, creating a broad array of in-between hues for smooth color transitions.
    """

    speed: int
    palette: Palette
    blend: bool
