# awtrix_light_client

## Install
```py
pip install awtrix_light_client
```

## Usage example

Official project documentation : https://blueforcer.github.io/awtrix-light/#/api

Available environment variables
```
AWTRIX_HTTP_CLIENT_AWTRIX="<AWTRIX CONFIG>"
```

`<AWTRIX CONFIG>` is in JSON and looks like this :
```json
{
    "base_url": "http://192.168.0.1",
    "username": "admin",
    "password": "password",
    "verify_ssl": false
}
```
`verify_ssl` used to verify https config (if accessing behind an HTTPS reverse proxy), can be `true`, `false`, or can point to a local ca bundle PEM encoded to validate local CA

Environment variables can also be placed in a `.env` in the working directory.

```py
import asyncio

from awtrix_light_client.http_client import get_awtrix_http_client, AwtrixLightHttpClientError


async def main():
    try:
        async with get_awtrix_http_client() as client:
            stats = await client.get_stats()
            print(stats)
    except AwtrixLightHttpClientError as e:
        print(f"HTTP code: {e.status_code}, error content: {e.content}")


asyncio.run(main())
```
