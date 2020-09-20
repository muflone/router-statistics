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

import importlib.util
import os.path

from router_statistics.profiles.base_model import BaseModel


class Router(object):
    def __init__(self,
                 profile: str,
                 destination: str,
                 username: str,
                 password: str):
        model_class = self._get_model_by_path(profile)
        self.model = model_class(destination, username, password)

    def _get_model_by_path(self, model_path: str) -> BaseModel:
        """
        Load the profile using `model_path` and return the model Class
        :param model_path: path for the requested model
        :return: BaseModel class with the specific requested model
        """
        full_path = os.path.abspath(os.path.join(__file__,
                                                 '..',
                                                 'profiles',
                                                 model_path))
        spec = importlib.util.spec_from_file_location('router_model_selected',
                                                      full_path + '.py')
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module.Model
