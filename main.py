#!/usr/bin/env python
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

import argparse
import getpass

from router_statistics.constants import APP_NAME, VERSION
from router_statistics.router import Router


def get_command_line_arguments() -> argparse.Namespace:
    """
    Get command line arguments
    :return: Namespace object with all the requested arguments
    """""
    parser = argparse.ArgumentParser()
    parser.add_argument('-P',
                        '--profile',
                        required=True,
                        help='Profile path')
    group = parser.add_argument_group(title='Router options')
    group.add_argument('-d',
                       '--destination',
                       required=True,
                       help='Router address (IP or FQDN)')
    group.add_argument('-u',
                       '--username',
                       required=True,
                       help='Router username')
    group.add_argument('-p',
                       '--password',
                       required=False,
                       help='Router password')
    group = parser.add_argument_group(title='Optional arguments')
    group.add_argument('-V',
                       '--version',
                       action='version',
                       version='{PROGRAM} {VERSION}'.format(PROGRAM=APP_NAME,
                                                            VERSION=VERSION))
    arguments = parser.parse_args()
    # Get password argument from command line
    if arguments.password == '-':
        arguments.password = getpass.getpass(
            'Please insert router password: ').encode('utf-8')
    return arguments


if __name__ == '__main__':
    # Get command line arguments
    arguments = get_command_line_arguments()

    # Get the requested model using the profile name
    router = Router(profile=arguments.profile,
                    destination=arguments.destination,
                    username=arguments.username,
                    password=arguments.password)
    # Execute actions
    with router as model:
        pass
