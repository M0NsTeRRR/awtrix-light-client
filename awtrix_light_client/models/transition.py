from enum import IntEnum


class TransitionType(IntEnum):
    RANDOM = 0
    SLIDE = 1
    DIM = 2
    ZOOM = 3
    ROTATE = 4
    PIXELATE = 5
    CURTAIN = 6
    RIPPLE = 7
    BLINK = 8
    RELOAD = 9
    FADE = 10
