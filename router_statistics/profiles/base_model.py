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

from .base_interface import BaseInterface


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

    def get_interface_lan(self) -> BaseInterface:
        """
        Get the LAN interface
        :return: LAN interface name
        """
        pass

    def get_interface_wan(self) -> BaseInterface:
        """
        Get the WAN interface
        :return: WAN interface name
        """
        pass
