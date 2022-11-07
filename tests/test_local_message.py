# glowprom
# Copyright (C) 2020 Andrew Wilkinson
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import json
import unittest

from glowprom.local_message import local_message


ELECTRIC_MESSAGE_TEXT = open("tests/test_local_electric_message.txt", "rb") \
                        .read()
GAS_MESSAGE_TEXT = open("tests/test_local_gas_message.txt", "rb").read()


class MockMessage:
    def __init__(self, payload):
        self.payload = payload


class TestLocalMessage(unittest.TestCase):
    def test_electric_message(self):
        prom = local_message(MockMessage(ELECTRIC_MESSAGE_TEXT))

        self.assertIn(
            "glowprom_import_cumulative_Wh{type=\"electric\", mpan=\"abcd\"}"
            + " 15254827.0", prom)

    def test_gas_message(self):
        prom = local_message(MockMessage(GAS_MESSAGE_TEXT))

        self.assertIn(
            "glowprom_import_cumulative_Wh{type=\"gas\", mprn=\"wxyz\"}"
            + " 66589570.00000001", prom)
