Python async HTTP client for [awtrix-light](https://github.com/Blueforcer/awtrix-light)

[![PyPI](https://img.shields.io/pypi/v/awtrix-light-client.svg)](https://pypi.python.org/pypi/awtrix-light-client)
[![PyPI versions](https://img.shields.io/pypi/pyversions/awtrix-light-client.svg)](https://pypi.python.org/pypi/awtrix-light-client)
[![Python test](https://github.com/M0NsTeRRR/awtrix-light-client/actions/workflows/test.yml/badge.svg)](https://github.com/M0NsTeRRR/awtrix-light-client/actions/workflows/test.yml)
[![Code Style](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)

# Warning
This client has been tested with awtrix-light v0.90 use with caution as official dev documentation is not fully documented and can cause crash

# Documentation
[https://M0NsTeRRR.github.io/awtrix-light-client](https://M0NsTeRRR.github.io/awtrix-light-client)

# Dev
Install [Poetry](https://python-poetry.org/docs/master/#installing-with-the-official-installer)

Install and setup dependencies
```
poetry install
poetry shell
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