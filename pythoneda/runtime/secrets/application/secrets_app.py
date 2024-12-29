# vim: set fileencoding=utf-8
"""
pythoneda/runtime/secrets/application/boot_app.py

This file defines the SecretsApp class.

Copyright (C) 2024-today boot's pythoneda-runtime/secrets-application

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import asyncio
from dbus_next import BusType
from pythoneda.shared.application import enable, PythonEDA
from pythoneda.shared.runtime.secrets.events.infrastructure.dbus import (
    DbusCredentialIssued,
    DbusCredentialProvided,
    DbusCredentialRequested,
)
from pythoneda.runtime.secrets.infrastructure.dbus import (
    SecretsDbusSignalEmitter,
    SecretsDbusSignalListener,
)


@enable(
    SecretsDbusSignalEmitter,
    events=[{"event-class": DbusCredentialProvided, "bus-type": BusType.SYSTEM}],
)
@enable(
    SecretsDbusSignalListener,
    events=[
        {
            "event-class": DbusCredentialIssued,
            "bus-type": BusType.SYSTEM,
        },
        {
            "event-class": DbusCredentialRequested,
            "bus-type": BusType.SYSTEM,
        },
    ],
)
class SecretsApp(PythonEDA):
    """
    Runs PythonEDA Secrets.

    Class name: SecretsApp

    Responsibilities:
        - Runs PythonEDA Secrets.

    Collaborators:
        - Command-line handlers from pythoneda-runtime/secrets-infrastructure
    """

    def __init__(self):
        """
        Creates a new SecretsApp instance.
        """
        # boot_banner is automatically generated by pythoneda-runtime-def/secrets-application
        try:
            from pythoneda.runtime.secrets.application.secrets_banner import (
                SecretsBanner,
            )

            banner = SecretsBanner()
        except ImportError:
            banner = None
        super().__init__("Secrets", banner, __file__)


if __name__ == "__main__":
    asyncio.run(SecretsApp.main("pythoneda.runtime.secrets.application.SecretsApp"))

# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
