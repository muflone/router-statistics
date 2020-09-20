##
#     Project: Router statitics
# Description: Access your router statistics
#      Author: Fabio Castelli (Muflone) <muflone@muflone.com>
#   Copyright: 2020 Fabio Castelli
#     License: GPL-3+
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
##

from ..base_interface import BaseInterface
from ..interface_type import InterfaceType
from ..system_info import SystemInfo


class BaseModel(object):
    def __init__(self, address: str, username: str, password: str):
        """
        Base model class to implement
        :param address: router address (IP or FQDN)
        :param username: username needed to authenticate
        :param password: password needed to authenticate
        """
        self.address = address
        self.username = username
        self.password = password
        self.interfaces = []
        self.info = SystemInfo()
        self.friendly_name = None

    def open(self):
        """
        Open the connection to the router
        """
        pass

    def close(self):
        """
        Close the connection to the router
        """
        pass

    def get_data(self) -> None:
        """
        Get data from the router
        :return: None
        """
        self.interfaces.clear()

    def get_system_info(self) -> SystemInfo:
        """
        Get the system information
        :return: SystemInfo object
        """
        return self.info

    def get_interfaces(self, type: InterfaceType) -> BaseInterface:
        """
        Get a list of interfaces of the supplied type
        :param type: interfaces type
        :return: list of interfaces
        """
        return [interface for interface in self.interfaces
                if interface.type == type]
