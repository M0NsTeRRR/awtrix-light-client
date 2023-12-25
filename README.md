Python async HTTP client for [awtrix-light](https://github.com/Blueforcer/awtrix-light)

[![PyPI](https://img.shields.io/pypi/v/awtrix-light-client.svg)](https://pypi.python.org/pypi/awtrix-light-client)
[![PyPI versions](https://img.shields.io/pypi/pyversions/awtrix-light-client.svg)](https://pypi.python.org/pypi/awtrix-light-client)
[![Python test](https://github.com/M0NsTeRRR/awtrix-light-client/actions/workflows/test.yml/badge.svg)](https://github.com/M0NsTeRRR/awtrix-light-client/actions/workflows/test.yml)
[![Code Style](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)

# Warning
This client has been tested with awtrix-light v0.90 use with caution as official dev documentation is not fully documented and can cause crash

# Install
```
pip install awtrix-light-client
```

# Dev
Install [Poetry](https://python-poetry.org/docs/master/#installing-with-the-official-installer)

Install and setup dependencies
```
poetry install
poetry shell
```

# Usage
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

Example script
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

### Run unit test
```
poetry run pytest --cov
```

### Run ruff
```
poetry run ruff format . 
poetry run ruff check .
```

## Contributing

We welcome and encourage contributions to this project! Please read the [Contributing guide](CONTRIBUTING.md). Also make sure to check the [Code of Conduct](CODE_OF_CONDUCT.md) and adhere to its guidelines

# Security

See [SECURITY.md](SECURITY.md) file for details.

# Licence

The code is under CeCILL license.

You can find all details here: https://cecill.info/licences/Licence_CeCILL_V2.1-en.html

# Credits

Copyright © Ludovic Ortega, 2023

Contributor(s):

-Ortega Ludovic - ludovic.ortega@adminafk.fr