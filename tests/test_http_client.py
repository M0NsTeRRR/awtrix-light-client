from typing import AsyncIterator

import pytest
from pydantic import ValidationError
from pydantic_extra_types.color import Color
from pytest_httpx import HTTPXMock

from awtrix_light_client.http_client import AwtrixLightHttpClient
from awtrix_light_client.models.stat import Stats
from awtrix_light_client.models.effect import EffectSetting, EffectType, Palette
from awtrix_light_client.models.transition import TransitionType
from awtrix_light_client.models.loop import Loop
from awtrix_light_client.models.screen import Screen
from awtrix_light_client.models.moodlight import Moodlight
from awtrix_light_client.models.setting import Settings
from awtrix_light_client.models.application import (
    CustomApplication,
    Notification,
    Fragment,
    TextCase,
    PushIcon,
    LifeTimeMode,
    Dp,
    Dl,
    Dr,
    Df,
    Dc,
    Dfc,
    Dt,
    Db,
)

BASE_URL = "http://test/api/"


async def test_get_stats(
    awtrix_http_client: AsyncIterator[AwtrixLightHttpClient], httpx_mock: HTTPXMock
):
    httpx_mock.add_response(
        method="GET",
        url=f"{BASE_URL}stats",
        json={
            "bat": 52,
            "bat_raw": 574,
            "type": 0,
            "lux": 0,
            "ldr_raw": 79,
            "ram": 144524,
            "bri": 120,
            "temp": 26,
            "hum": 45,
            "uptime": 461,
            "wifi_signal": -53,
            "messages": 0,
            "version": "0.90",
            "indicator1": False,
            "indicator2": False,
            "indicator3": False,
            "app": "Time",
            "uid": "awtrix_fa9b04",
            "matrix": True,
        },
    )

    async with awtrix_http_client as client:
        assert await client.get_stats() == Stats(
            bat=52,
            bat_raw=574,
            type=0,
            lux=0,
            ldr_raw=79,
            ram=144524,
            bri=120,
            temp=26,
            hum=45,
            uptime=461,
            wifi_signal=-53,
            messages=0,
            version="0.90",
            indicator1=False,
            indicator2=False,
            indicator3=False,
            app="Time",
            uid="awtrix_fa9b04",
            matrix=True,
        )


async def test_get_effects(
    awtrix_http_client: AsyncIterator[AwtrixLightHttpClient], httpx_mock: HTTPXMock
):
    httpx_mock.add_response(
        method="GET",
        url=f"{BASE_URL}effects",
        json=[
            "Fade",
            "MovingLine",
            "BrickBreaker",
            "PingPong",
            "Radar",
            "Checkerboard",
            "Fireworks",
            "PlasmaCloud",
            "Ripple",
            "Snake",
            "Pacifica",
            "TheaterChase",
            "Plasma",
            "Matrix",
            "SwirlIn",
            "SwirlOut",
            "LookingEyes",
            "TwinklingStars",
            "ColorWaves",
        ],
    )

    async with awtrix_http_client as client:
        assert await client.get_effects() == [
            EffectType("Fade"),
            EffectType("MovingLine"),
            EffectType("BrickBreaker"),
            EffectType("PingPong"),
            EffectType("Radar"),
            EffectType("Checkerboard"),
            EffectType("Fireworks"),
            EffectType("PlasmaCloud"),
            EffectType("Ripple"),
            EffectType("Snake"),
            EffectType("Pacifica"),
            EffectType("TheaterChase"),
            EffectType("Plasma"),
            EffectType("Matrix"),
            EffectType("SwirlIn"),
            EffectType("SwirlOut"),
            EffectType("LookingEyes"),
            EffectType("TwinklingStars"),
            EffectType("ColorWaves"),
        ]


async def test_get_transitions(
    awtrix_http_client: AsyncIterator[AwtrixLightHttpClient], httpx_mock: HTTPXMock
):
    httpx_mock.add_response(
        method="GET",
        url=f"{BASE_URL}transitions",
        json=[
            "Random",
            "Slide",
            "Dim",
            "Zoom",
            "Rotate",
            "Pixelate",
            "Curtain",
            "Ripple",
            "Blink",
            "Reload",
            "Fade",
        ],
    )

    async with awtrix_http_client as client:
        assert await client.get_transitions() == [
            TransitionType["RANDOM"],
            TransitionType["SLIDE"],
            TransitionType["DIM"],
            TransitionType["ZOOM"],
            TransitionType["ROTATE"],
            TransitionType["PIXELATE"],
            TransitionType["CURTAIN"],
            TransitionType["RIPPLE"],
            TransitionType["BLINK"],
            TransitionType["RELOAD"],
            TransitionType["FADE"],
        ]


async def test_get_loops(
    awtrix_http_client: AsyncIterator[AwtrixLightHttpClient], httpx_mock: HTTPXMock
):
    httpx_mock.add_response(
        method="GET",
        url=f"{BASE_URL}loop",
        json={"Time": 0, "Temperature": 1, "Humidity": 2, "Battery": 3},
    )

    async with awtrix_http_client as client:
        assert await client.get_loops() == Loop(
            loops=[
                "Time",
                "Temperature",
                "Humidity",
                "Battery",
            ]
        )


async def test_get_screen(
    awtrix_http_client: AsyncIterator[AwtrixLightHttpClient], httpx_mock: HTTPXMock
):
    httpx_mock.add_response(
        method="GET",
        url=f"{BASE_URL}screen",
        json=[
            0,
            0,
            65280,
            65280,
            65280,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            65280,
            65280,
            77826,
            65280,
            65280,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            16777215,
            0,
            16777215,
            0,
            16777215,
            16777215,
            16777215,
            0,
            16777215,
            0,
            16777215,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            65280,
            77826,
            77826,
            77826,
            65280,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            16777215,
            0,
            16777215,
            0,
            0,
            0,
            16777215,
            0,
            0,
            0,
            16777215,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            65280,
            77826,
            77826,
            77826,
            65280,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            16777215,
            16777215,
            16777215,
            0,
            16777215,
            16777215,
            16777215,
            0,
            0,
            16777215,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            65280,
            77826,
            77826,
            77826,
            65280,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            16777215,
            0,
            0,
            0,
            16777215,
            0,
            16777215,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            65280,
            77826,
            77826,
            77826,
            65280,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            16777215,
            0,
            16777215,
            16777215,
            16777215,
            0,
            16777215,
            0,
            16777215,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            65280,
            77826,
            77826,
            77826,
            65280,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            263168,
            65280,
            65280,
            65280,
            65280,
            65280,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
        ],
    )

    async with awtrix_http_client as client:
        assert await client.get_screen() == Screen(
            matrix=[
                0,
                0,
                65280,
                65280,
                65280,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                65280,
                65280,
                77826,
                65280,
                65280,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                16777215,
                0,
                16777215,
                0,
                16777215,
                16777215,
                16777215,
                0,
                16777215,
                0,
                16777215,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                65280,
                77826,
                77826,
                77826,
                65280,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                16777215,
                0,
                16777215,
                0,
                0,
                0,
                16777215,
                0,
                0,
                0,
                16777215,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                65280,
                77826,
                77826,
                77826,
                65280,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                16777215,
                16777215,
                16777215,
                0,
                16777215,
                16777215,
                16777215,
                0,
                0,
                16777215,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                65280,
                77826,
                77826,
                77826,
                65280,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                16777215,
                0,
                0,
                0,
                16777215,
                0,
                16777215,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                65280,
                77826,
                77826,
                77826,
                65280,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                16777215,
                0,
                16777215,
                16777215,
                16777215,
                0,
                16777215,
                0,
                16777215,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                65280,
                77826,
                77826,
                77826,
                65280,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                263168,
                65280,
                65280,
                65280,
                65280,
                65280,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
            ]
        )


async def test_set_power(
    awtrix_http_client: AsyncIterator[AwtrixLightHttpClient], httpx_mock: HTTPXMock
):
    httpx_mock.add_response(
        method="POST",
        url=f"{BASE_URL}power",
        match_json={"power": False},
    )

    async with awtrix_http_client as client:
        assert await client.set_power(False) == None


async def test_set_sleep(
    awtrix_http_client: AsyncIterator[AwtrixLightHttpClient], httpx_mock: HTTPXMock
):
    httpx_mock.add_response(
        method="POST",
        url=f"{BASE_URL}sleep",
        match_json={"sleep": 10},
    )

    async with awtrix_http_client as client:
        assert await client.set_sleep(10) == None


async def test_set_sound(
    awtrix_http_client: AsyncIterator[AwtrixLightHttpClient], httpx_mock: HTTPXMock
):
    httpx_mock.add_response(
        method="POST",
        url=f"{BASE_URL}sound",
        match_json={"sound": "alarm"},
    )

    async with awtrix_http_client as client:
        assert await client.set_sound("alarm") == None


async def test_set_rtttl(
    awtrix_http_client: AsyncIterator[AwtrixLightHttpClient], httpx_mock: HTTPXMock
):
    httpx_mock.add_response(
        method="POST",
        url=f"{BASE_URL}rtttl",
        match_json={
            "rtttl": "JingleBell:d=8,o=5,b=112:32p,a,a,4a,a,a,4a,a,c6,f.,16g,2a,a#,a#,a#.,16a#,a#,a,a.,16a,a,g,g,a,4g,4c6"
        },
    )

    async with awtrix_http_client as client:
        assert (
            await client.set_rtttl(
                "JingleBell:d=8,o=5,b=112:32p,a,a,4a,a,a,4a,a,c6,f.,16g,2a,a#,a#,a#.,16a#,a#,a,a.,16a,a,g,g,a,4g,4c6"
            )
            == None
        )


async def test_wrong_moodlight():
    with pytest.raises(ValidationError, match="kelvin and color can't be set together"):
        Moodlight(brightness=170, kelvin=2300, color=Color("#FF00FF"))


async def test_set_moodlight(
    awtrix_http_client: AsyncIterator[AwtrixLightHttpClient], httpx_mock: HTTPXMock
):
    httpx_mock.add_response(
        method="POST",
        url=f"{BASE_URL}moodlight",
        match_json={"brightness": 170, "color": "#FF00FF"},
    )

    async with awtrix_http_client as client:
        assert (
            await client.set_moodlight(
                Moodlight(brightness=170, color=Color("#FF00FF"))
            )
            == None
        )


async def test_wrong_indicator_param(
    awtrix_http_client: AsyncIterator[AwtrixLightHttpClient],
):
    with pytest.raises(ValueError, match="fade and blink can't be set together"):
        async with awtrix_http_client as client:
            assert (
                await client.set_indicator(2, color=Color("#FF00FF"), fade=2, blink=2)
                == None
            )


async def test_set_indicator(
    awtrix_http_client: AsyncIterator[AwtrixLightHttpClient], httpx_mock: HTTPXMock
):
    httpx_mock.add_response(
        method="POST",
        url=f"{BASE_URL}indicator2",
        match_json={"color": "#FF00FF", "fade": 2},
    )

    async with awtrix_http_client as client:
        assert await client.set_indicator(2, color=Color("#FF00FF"), fade=2) == None


async def test_set_one_custom_application(
    awtrix_http_client: AsyncIterator[AwtrixLightHttpClient], httpx_mock: HTTPXMock
):
    httpx_mock.add_response(
        method="POST",
        url=f"{BASE_URL}custom?name=test",
        match_json={
            "text": [{"t": "test", "c": "#0000FF"}],
            "textCase": 0,
            "topText": True,
            "textOffset": 2,
            "center": True,
            "color": "#0000FF",
            "gradient": ["#0000FF", "#0000FF"],
            "background": "#0000FF",
            "rainbow": True,
            "icon": "4300",
            "pushIcon": 0,
            "repeat": 50,
            "duration": 50,
            "bar": [12],
            "line": [12],
            "autoscale": True,
            "progress": 50,
            "progressC": "#0000FF",
            "progressBC": "#0000FF",
            "pos": 2,
            "draw": [
                {"x": 0, "y": 0, "cl": "#0000FF"},
                {"x0": 1, "y0": 1, "x1": 1, "y1": 1, "cl": "#0000FF"},
                {"x": 2, "y": 2, "w": 2, "h": 2, "cl": "#0000FF"},
                {"x": 3, "y": 3, "w": 3, "h": 3, "cl": "#0000FF"},
                {"x": 4, "y": 4, "r": 4, "cl": "#0000FF"},
                {"x": 5, "y": 5, "r": 2, "cl": "#0000FF"},
                {"x": 6, "y": 6, "t": 6, "cl": "#0000FF"},
                {"x": 7, "y": 7, "r": 7, "cl": "#0000FF"},
            ],
            "noScroll": True,
            "scrollSpeed": 50,
            "effect": "Fade",
            "effectSettings": {"speed": 1, "palette": "Lava", "blend": True},
            "lifetime": 2,
            "lifetimeMode": 1,
            "save": True,
        },
    )

    async with awtrix_http_client as client:
        assert (
            await client.set_custom_application(
                "test",
                CustomApplication(
                    text=[Fragment(t="test", c=Color("blue"))],
                    textCase=TextCase.GLOBAL,
                    topText=True,
                    textOffset=2,
                    center=True,
                    color=Color("blue"),
                    gradient=[Color("blue"), Color("blue")],
                    background=Color("blue"),
                    rainbow=True,
                    icon="4300",
                    pushIcon=PushIcon.NOT_MOVING,
                    repeat=50,
                    duration=50,
                    bar=[12],
                    line=[12],
                    autoscale=True,
                    progress=50,
                    progressC=Color("blue"),
                    progressBC=Color("blue"),
                    pos=2,
                    draw=[
                        Dp(x=0, y=0, cl=Color("blue")),
                        Dl(x0=1, y0=1, x1=1, y1=1, cl=Color("blue")),
                        Dr(x=2, y=2, w=2, h=2, cl=Color("blue")),
                        Df(x=3, y=3, w=3, h=3, cl=Color("blue")),
                        Dc(x=4, y=4, r=4, cl=Color("blue")),
                        Dfc(x=5, y=5, r=2, cl=Color("blue")),
                        Dt(x=6, y=6, t=6, cl=Color("blue")),
                        Db(x=7, y=7, r=7, cl=Color("blue")),
                    ],
                    lifetime=2,
                    lifetimeMode=LifeTimeMode.STALE,
                    noScroll=True,
                    scrollSpeed=50,
                    effect=EffectType.FADE,
                    effectSettings=EffectSetting(
                        speed=1, palette=Palette.LAVA, blend=True
                    ),
                    save=True,
                ),
            )
            == None
        )


async def test_set_multiple_custom_application(
    awtrix_http_client: AsyncIterator[AwtrixLightHttpClient], httpx_mock: HTTPXMock
):
    httpx_mock.add_response(
        method="POST",
        url=f"{BASE_URL}custom?name=test",
        match_json=[
            {
                "text": [{"t": "test", "c": "#0000FF"}],
                "textCase": 0,
                "topText": True,
                "textOffset": 2,
                "center": True,
                "color": "#0000FF",
                "gradient": ["#0000FF", "#0000FF"],
                "background": "#0000FF",
                "rainbow": True,
                "icon": "4300",
                "pushIcon": 0,
                "repeat": 50,
                "duration": 50,
                "bar": [12],
                "line": [12],
                "autoscale": True,
                "progress": 50,
                "progressC": "#0000FF",
                "progressBC": "#0000FF",
                "draw": [
                    {"x": 0, "y": 0, "cl": "#0000FF"},
                    {"x0": 1, "y0": 1, "x1": 1, "y1": 1, "cl": "#0000FF"},
                    {"x": 2, "y": 2, "w": 2, "h": 2, "cl": "#0000FF"},
                    {"x": 3, "y": 3, "w": 3, "h": 3, "cl": "#0000FF"},
                    {"x": 4, "y": 4, "r": 4, "cl": "#0000FF"},
                    {"x": 5, "y": 5, "r": 2, "cl": "#0000FF"},
                    {"x": 6, "y": 6, "t": 6, "cl": "#0000FF"},
                    {"x": 7, "y": 7, "r": 7, "cl": "#0000FF"},
                ],
                "noScroll": True,
                "scrollSpeed": 50,
                "effect": "Fade",
                "effectSettings": {"speed": 1, "palette": "Lava", "blend": True},
                "pos": 2,
                "lifetime": 2,
                "lifetimeMode": 1,
                "save": True,
            }
        ],
    )

    async with awtrix_http_client as client:
        assert (
            await client.set_custom_application(
                "test",
                [
                    CustomApplication(
                        text=[Fragment(t="test", c=Color("blue"))],
                        textCase=TextCase.GLOBAL,
                        topText=True,
                        textOffset=2,
                        center=True,
                        color=Color("blue"),
                        gradient=[Color("blue"), Color("blue")],
                        background=Color("blue"),
                        rainbow=True,
                        icon="4300",
                        pushIcon=PushIcon.NOT_MOVING,
                        repeat=50,
                        duration=50,
                        bar=[12],
                        line=[12],
                        autoscale=True,
                        progress=50,
                        progressC=Color("blue"),
                        progressBC=Color("blue"),
                        pos=2,
                        draw=[
                            Dp(x=0, y=0, cl=Color("blue")),
                            Dl(x0=1, y0=1, x1=1, y1=1, cl=Color("blue")),
                            Dr(x=2, y=2, w=2, h=2, cl=Color("blue")),
                            Df(x=3, y=3, w=3, h=3, cl=Color("blue")),
                            Dc(x=4, y=4, r=4, cl=Color("blue")),
                            Dfc(x=5, y=5, r=2, cl=Color("blue")),
                            Dt(x=6, y=6, t=6, cl=Color("blue")),
                            Db(x=7, y=7, r=7, cl=Color("blue")),
                        ],
                        lifetime=2,
                        lifetimeMode=LifeTimeMode.STALE,
                        noScroll=True,
                        scrollSpeed=50,
                        effect=EffectType.FADE,
                        effectSettings=EffectSetting(
                            speed=1, palette=Palette.LAVA, blend=True
                        ),
                        save=True,
                    )
                ],
            )
            == None
        )


async def test_notify(
    awtrix_http_client: AsyncIterator[AwtrixLightHttpClient], httpx_mock: HTTPXMock
):
    httpx_mock.add_response(
        method="POST",
        url=f"{BASE_URL}notify",
        match_json={
            "text": [{"t": "test", "c": "#0000FF"}],
            "textCase": 0,
            "topText": True,
            "textOffset": 2,
            "center": True,
            "color": "#0000FF",
            "gradient": ["#0000FF", "#0000FF"],
            "background": "#0000FF",
            "rainbow": True,
            "icon": "4300",
            "pushIcon": 0,
            "repeat": 50,
            "duration": 50,
            "bar": [12],
            "line": [12],
            "autoscale": True,
            "progress": 50,
            "progressC": "#0000FF",
            "progressBC": "#0000FF",
            "draw": [
                {"x": 0, "y": 0, "cl": "#0000FF"},
                {"x0": 1, "y0": 1, "x1": 1, "y1": 1, "cl": "#0000FF"},
                {"x": 2, "y": 2, "w": 2, "h": 2, "cl": "#0000FF"},
                {"x": 3, "y": 3, "w": 3, "h": 3, "cl": "#0000FF"},
                {"x": 4, "y": 4, "r": 4, "cl": "#0000FF"},
                {"x": 5, "y": 5, "r": 2, "cl": "#0000FF"},
                {"x": 6, "y": 6, "t": 6, "cl": "#0000FF"},
                {"x": 7, "y": 7, "r": 7, "cl": "#0000FF"},
            ],
            "noScroll": True,
            "scrollSpeed": 50,
            "effect": "Fade",
            "effectSettings": {"speed": 1, "palette": "Lava", "blend": True},
            "hold": True,
            "sound": "test",
            "loopSound": True,
            "stack": True,
            "wakeup": True,
            "clients": ["http://test.fr/"],
        },
    )

    async with awtrix_http_client as client:
        assert (
            await client.notify(
                Notification(
                    text=[Fragment(t="test", c=Color("blue"))],
                    textCase=TextCase.GLOBAL,
                    topText=True,
                    textOffset=2,
                    center=True,
                    color=Color("blue"),
                    gradient=[Color("blue"), Color("blue")],
                    background=Color("blue"),
                    rainbow=True,
                    icon="4300",
                    pushIcon=PushIcon.NOT_MOVING,
                    repeat=50,
                    duration=50,
                    bar=[12],
                    line=[12],
                    autoscale=True,
                    progress=50,
                    progressC=Color("blue"),
                    progressBC=Color("blue"),
                    draw=[
                        Dp(x=0, y=0, cl=Color("blue")),
                        Dl(x0=1, y0=1, x1=1, y1=1, cl=Color("blue")),
                        Dr(x=2, y=2, w=2, h=2, cl=Color("blue")),
                        Df(x=3, y=3, w=3, h=3, cl=Color("blue")),
                        Dc(x=4, y=4, r=4, cl=Color("blue")),
                        Dfc(x=5, y=5, r=2, cl=Color("blue")),
                        Dt(x=6, y=6, t=6, cl=Color("blue")),
                        Db(x=7, y=7, r=7, cl=Color("blue")),
                    ],
                    noScroll=True,
                    scrollSpeed=50,
                    effect=EffectType.FADE,
                    effectSettings=EffectSetting(
                        speed=1, palette=Palette.LAVA, blend=True
                    ),
                    hold=True,
                    sound="test",
                    loopSound=True,
                    stack=True,
                    wakeup=True,
                    clients=["http://test.fr"],
                )
            )
            == None
        )


async def test_dismiss_notification(
    awtrix_http_client: AsyncIterator[AwtrixLightHttpClient], httpx_mock: HTTPXMock
):
    httpx_mock.add_response(
        method="POST",
        url=f"{BASE_URL}notify/dismiss",
    )

    async with awtrix_http_client as client:
        assert await client.dismiss_notification() == None


async def test_next_app(
    awtrix_http_client: AsyncIterator[AwtrixLightHttpClient], httpx_mock: HTTPXMock
):
    httpx_mock.add_response(
        method="POST",
        url=f"{BASE_URL}nextapp",
    )

    async with awtrix_http_client as client:
        assert await client.next_app() == None


async def test_previous_app(
    awtrix_http_client: AsyncIterator[AwtrixLightHttpClient], httpx_mock: HTTPXMock
):
    httpx_mock.add_response(
        method="POST",
        url=f"{BASE_URL}previousapp",
    )

    async with awtrix_http_client as client:
        assert await client.previous_app() == None


async def test_switch_app(
    awtrix_http_client: AsyncIterator[AwtrixLightHttpClient], httpx_mock: HTTPXMock
):
    httpx_mock.add_response(
        method="POST",
        url=f"{BASE_URL}switch",
        match_json={"name": "time"},
    )

    async with awtrix_http_client as client:
        assert await client.switch_app("time") == None


async def test_get_settings(
    awtrix_http_client: AsyncIterator[AwtrixLightHttpClient], httpx_mock: HTTPXMock
):
    httpx_mock.add_response(
        method="GET",
        url=f"{BASE_URL}settings",
        json={
            "MATP": True,
            "ABRI": False,
            "BRI": 120,
            "ATRANS": True,
            "TCOL": 16777215,
            "TEFF": 1,
            "TSPEED": 400,
            "ATIME": 7,
            "TMODE": 1,
            "CHCOL": 16711680,
            "CTCOL": 0,
            "CBCOL": 16777215,
            "TFORMAT": "%H %M",
            "DFORMAT": "%d.%m.%y",
            "SOM": True,
            "CEL": True,
            "BLOCKN": False,
            "MAT": 0,
            "SOUND": True,
            "GAMMA": 1.899999976,
            "UPPERCASE": True,
            "CCORRECTION": "#000000",
            "CTEMP": "#000000",
            "WD": True,
            "WDCA": 16777215,
            "WDCI": 6710886,
            "TIME_COL": 0,
            "DATE_COL": 0,
            "HUM_COL": 0,
            "TEMP_COL": 0,
            "BAT_COL": 0,
            "SSPEED": 100,
            "TIM": True,
            "DAT": False,
            "HUM": True,
            "TEMP": True,
            "BAT": True,
        },
    )

    async with awtrix_http_client as client:
        assert await client.get_settings() == Settings(
            ATIME=7,
            TEFF=TransitionType.SLIDE,
            TSPEED=400,
            TCOL=Color("#FFFFFF"),
            TMODE=1,
            CHCOL=Color("#FF0000"),
            CBCOL=Color("#FFFFFF"),
            CTCOL=0,
            WD=True,
            WDCA=Color("#FFFFFF"),
            WDCI=Color("#666666"),
            BRI=120,
            ABRI=False,
            ATRANS=True,
            CCORRECTION=Color("#000000"),
            CTEMP=Color("#000000"),
            TFORMAT="%H %M",
            DFORMAT="%d.%m.%y",
            SOM=True,
            CEL=True,
            MAT=0,
            SOUND=True,
            GAMMA=1.899999976,
            BLOCKN=False,
            UPPERCASE=True,
            TIME_COL=0,
            DATE_COL=0,
            TEMP_COL=0,
            HUM_COL=0,
            BAT_COL=0,
            SSPEED=100,
            TIM=True,
            DAT=False,
            HUM=True,
            TEMP=True,
            BAT=True,
            MATP=True,
        )


async def test_set_settings_all_params_optionnal(
    awtrix_http_client: AsyncIterator[AwtrixLightHttpClient], httpx_mock: HTTPXMock
):
    httpx_mock.add_response(
        method="POST",
        url=f"{BASE_URL}notify",
        match_json={},
    )

    async with awtrix_http_client as client:
        assert await client.notify(Notification()) == None


async def test_set_settings(
    awtrix_http_client: AsyncIterator[AwtrixLightHttpClient], httpx_mock: HTTPXMock
):
    httpx_mock.add_response(
        method="POST",
        url=f"{BASE_URL}settings",
        match_json={
            "MATP": True,
            "ABRI": False,
            "BRI": 120,
            "ATRANS": True,
            "TCOL": 16777215,
            "TEFF": 1,
            "TSPEED": 400,
            "ATIME": 7,
            "TMODE": 1,
            "CHCOL": 16711680,
            "CTCOL": 0,
            "CBCOL": 16777215,
            "TFORMAT": "%H %M",
            "DFORMAT": "%d.%m.%y",
            "SOM": True,
            "CEL": True,
            "BLOCKN": False,
            "MAT": 0,
            "SOUND": True,
            "GAMMA": 1.899999976,
            "UPPERCASE": True,
            "CCORRECTION": "#000000",
            "CTEMP": "#000000",
            "WD": True,
            "WDCA": 16777215,
            "WDCI": 6710886,
            "TIME_COL": 0,
            "DATE_COL": 0,
            "HUM_COL": 0,
            "TEMP_COL": 0,
            "BAT_COL": 0,
            "SSPEED": 100,
            "TIM": True,
            "DAT": False,
            "HUM": True,
            "TEMP": True,
            "BAT": True,
        },
    )

    async with awtrix_http_client as client:
        assert (
            await client.set_settings(
                Settings(
                    ATIME=7,
                    TEFF=TransitionType.SLIDE,
                    TSPEED=400,
                    TCOL=Color("#FFFFFF"),
                    TMODE=1,
                    CHCOL=Color("#FF0000"),
                    CBCOL=Color("#FFFFFF"),
                    CTCOL=0,
                    WD=True,
                    WDCA=Color("#FFFFFF"),
                    WDCI=Color("#666666"),
                    BRI=120,
                    ABRI=False,
                    ATRANS=True,
                    CCORRECTION=Color("#000000"),
                    CTEMP=Color("#000000"),
                    TFORMAT="%H %M",
                    DFORMAT="%d.%m.%y",
                    SOM=True,
                    CEL=True,
                    MAT=0,
                    SOUND=True,
                    GAMMA=1.899999976,
                    BLOCKN=False,
                    UPPERCASE=True,
                    TIME_COL=0,
                    DATE_COL=0,
                    TEMP_COL=0,
                    HUM_COL=0,
                    BAT_COL=0,
                    SSPEED=100,
                    TIM=True,
                    DAT=False,
                    HUM=True,
                    TEMP=True,
                    BAT=True,
                    MATP=True,
                )
            )
            == None
        )


async def test_update(
    awtrix_http_client: AsyncIterator[AwtrixLightHttpClient], httpx_mock: HTTPXMock
):
    httpx_mock.add_response(
        method="POST",
        url=f"{BASE_URL}doupdate",
    )

    async with awtrix_http_client as client:
        assert await client.update() == None


async def test_reboot(
    awtrix_http_client: AsyncIterator[AwtrixLightHttpClient], httpx_mock: HTTPXMock
):
    httpx_mock.add_response(
        method="POST",
        url=f"{BASE_URL}reboot",
    )

    async with awtrix_http_client as client:
        assert await client.reboot() == None


async def test_erase(
    awtrix_http_client: AsyncIterator[AwtrixLightHttpClient], httpx_mock: HTTPXMock
):
    httpx_mock.add_response(
        method="POST",
        url=f"{BASE_URL}erase",
    )

    async with awtrix_http_client as client:
        assert await client.erase() == None


async def test_reset_settings(
    awtrix_http_client: AsyncIterator[AwtrixLightHttpClient], httpx_mock: HTTPXMock
):
    httpx_mock.add_response(
        method="POST",
        url=f"{BASE_URL}resetSettings",
    )

    async with awtrix_http_client as client:
        assert await client.reset_settings() == None
