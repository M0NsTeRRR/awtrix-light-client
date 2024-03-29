from typing import Dict, Any, List, Union, Literal
from contextlib import asynccontextmanager
from typing import AsyncIterator

from httpx import AsyncClient
from pydantic_extra_types.color import Color

from .http_settings import AwtrixLightHttpClientSettings
from .models.stat import Stats
from .models.effect import EffectType
from .models.transition import TransitionType
from .models.loop import Loop
from .models.screen import Screen
from .models.moodlight import Moodlight
from .models.application import CustomApplication, Notification
from .models.setting import Settings


class AwtrixLightHttpClientError(BaseException):
    """Class of API exception

    :param status_code: HTTP status code of the response
    :param content: HTTP content of the response
    """

    def __init__(self, status_code: int, content: str, *args: object) -> None:
        super().__init__(*args)
        self.status_code = status_code
        self.content = content


class AwtrixLightHttpClient:
    def __init__(self, client: AsyncClient) -> None:
        """
        :param client: `AsyncClient`
        """
        self._client = client

    async def _make_request(
        self,
        method: str,
        url: str,
        params: Dict[Any, Any] = None,
        data: Dict[Any, Any] = None,
    ):
        """Boilerplate to make request to the APU. Handling error is done for you here."""
        r = await self._client.request(method, url, params=params, json=data)

        if not r.is_success:
            raise AwtrixLightHttpClientError(
                status_code=r.status_code, content=r.content
            )
        return r

    async def get_stats(self) -> Stats:
        """
        General device stats (e.g., battery, RAM)
        :return: Return a `Stats` object
        """
        response = (await self._make_request("GET", "stats")).json()

        return Stats(**response)

    async def get_effects(self) -> List[EffectType]:
        """
        List of all effects
        :return: Return a list of `EffectType` object
        """
        response = (await self._make_request("GET", "effects")).json()

        return [EffectType(e) for e in response]

    async def get_transitions(self) -> List[TransitionType]:
        """
        List of all transition effects
        :return: Return a list of `TransitionType` object
        """
        response = (await self._make_request("GET", "transitions")).json()

        return [(TransitionType[t.upper()]) for t in response]

    async def get_loops(self) -> Loop:
        """
        List of all apps in the loop
        :return: Return a `Loop` object
        """
        response = (await self._make_request("GET", "loop")).json()

        sorted_apps = dict(sorted(response.items(), key=lambda item: item[1]))

        return Loop(loops=[app for app in sorted_apps.keys()])

    async def get_screen(self) -> Screen:
        """
        Retrieve the current matrix screen as an array of 24 bit colors
        :return: Return a `Screen` object
        """
        response = (await self._make_request("GET", "screen")).json()

        return Screen(matrix=response)

    async def set_power(self, power: bool) -> None:
        """
        Toggle the matrix on or off
        :param power: Toggle the matrix
        """
        await self._make_request("POST", "power", data={"power": power})

    async def set_sleep(self, seconds: int) -> None:
        """
        Send the board in deep sleep mode (turns off the matrix as well), good for saving battery life
        :param seconds: Duration of sleep mode
        """
        await self._make_request("POST", "sleep", data={"sleep": seconds})

    async def set_sound(self, sound: str) -> None:
        """
        Play a RTTTL sound from the MELODIES folder
        :param sound: Sound to play
        """
        await self._make_request("POST", "sound", data={"sound": sound})

    async def set_rtttl(self, rtttl: str) -> None:
        """
        Play a RTTTL sound from a given RTTTL string
        :param sound: Sound to play in RTTTL format
        """
        await self._make_request("POST", "rtttl", data={"rtttl": rtttl})

    async def set_moodlight(self, moodlight: Moodlight) -> None:
        """
        Set the entire matrix to a custom color or temperature
        :param moodlight: Custom color or temperature to set. To disable moodlight pass an empty object `Moodlight()`
        """
        await self._make_request(
            "POST", "moodlight", data=moodlight.model_dump(exclude_none=True)
        )

    async def set_indicator(
        self,
        indicator: Literal[1, 2, 3],
        color: Color,
        blink: int = None,
        fade: int = None,
    ) -> None:
        """
        Colored indicators serve as small notification signs displayed on specific areas of the screen:
        :param indicator: Indicator (Upper right corner = 1, Right side = 2, Lower right corner = 3)
        :param color: Color to display. To hide the indicators pass black as Color
        :param blink: Blink timer in milliseconds
        :param fade: Fade timer in milliseconds
        """
        if blink and fade:
            raise ValueError("fade and blink can't be set together")

        data = {"color": color.as_hex(format="long").upper()}

        if blink:
            data["blink"] = blink

        if fade:
            data["fade"] = fade

        await self._make_request(
            "POST",
            f"indicator{indicator}",
            data=data,
        )

    async def set_custom_application(
        self,
        name: str,
        custom_application: Union[CustomApplication, List[CustomApplication], None],
    ) -> None:
        """
        Set custom app or a list of custom app
        When erasing apps, AWTRIX doesn't match the exact app name. Instead, it identifies apps that begin with the specified name.
        To expunge all associated apps, send application=None. For example for name=test. This action will remove test0, test1, and so on.
        To eradicate a single app, direct the command to, for instance, test1
        :param name: Name of the application to manage
        :param custom_application: An application, a list of application to setup or None
        """
        if isinstance(custom_application, CustomApplication):
            data = custom_application.model_dump(exclude_none=True)
        else:
            data = [app.model_dump(exclude_none=True) for app in custom_application]

        await self._make_request("POST", "custom", params={"name": name}, data=data)

    async def notify(self, notification: Notification) -> None:
        """
        One-Time Notification
        :param notification: Notification to display
        """
        await self._make_request(
            "POST", "notify", data=notification.model_dump(exclude_none=True)
        )

    async def dismiss_notification(self) -> None:
        """
        Easily dismiss a notification that was configured with "hold": true
        """
        await self._make_request("POST", "notify/dismiss")

    async def next_app(self) -> None:
        """
        Navigate to the next app
        """
        await self._make_request("POST", "nextapp")

    async def previous_app(self) -> None:
        """
        Navigate to the previous app
        """
        await self._make_request("POST", "previousapp")

    async def switch_app(self, name: str) -> None:
        """
        Directly transition to a desired app using its name
        :param name: Application to switch to
        """
        await self._make_request("POST", "switch", data={"name": name})

    async def get_settings(self) -> Settings:
        """
        You can initiate the firmware update either through the update button in HA or using the following
        :return: Return a `Settings` object
        """
        return Settings(**(await self._make_request("GET", "settings")).json())

    async def set_settings(self, s: Settings) -> None:
        """
        Adjust various settings related to the app display.
        :param s: Settings to update
        """
        await self._make_request(
            "POST", "settings", data=s.model_dump(exclude_none=True)
        )

    async def update(self) -> None:
        """
        You can initiate the firmware update either through the update button in HA or using the following
        """
        await self._make_request("POST", "doupdate")

    async def reboot(self) -> None:
        """
        If you need to restart the Awtrix
        """
        await self._make_request("POST", "reboot")

    async def erase(self) -> None:
        """
        WARNING: This action will format the flash memory and EEPROM but will not modify the WiFi Settings. It essentially serves as a factory reset.
        """
        await self._make_request("POST", "erase")

    async def reset_settings(self) -> None:
        """
        WARNING: This action will reset all settings from the settings API. It does not reset the flash files and WiFi Settings.
        """
        await self._make_request("POST", "resetSettings")


@asynccontextmanager
async def get_awtrix_http_client() -> AsyncIterator[AwtrixLightHttpClient]:
    """Gives access to an instance of the Awtrix-light HTTP client

    :return: An `asynccontextmanager` of `AwtrixLightHttpClient`
    """
    settings = AwtrixLightHttpClientSettings()

    auth = None
    if settings.awtrix.username and settings.awtrix.password:
        auth = (
            settings.awtrix.username,
            settings.awtrix.password,
        )

    async with AsyncClient(
        base_url=f"{settings.awtrix.base_url}api",
        auth=auth,
        verify=settings.awtrix.verify_ssl,
    ) as client:
        yield AwtrixLightHttpClient(client)
