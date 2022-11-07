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

from glowprom.cloud_message import cloud_message


MESSAGE_TEXT = open("tests/test_message.txt", "rb").read()


class MockMessage:
    def __init__(self, payload):
        self.payload = payload


class TestCloudMessage(unittest.TestCase):
    def test_cloud_message(self):
        prom = cloud_message(MockMessage(MESSAGE_TEXT))

        self.assertIn(
            "glowprom_consumption{type=\"electricity\",period=\"daily\"} "
            + "7.971", prom)
        self.assertIn(
            "glowprom_consumption{type=\"gas\",period=\"daily\"} 39.452",
            prom)

    def test_missing_electricity(self):
        data = json.loads(MESSAGE_TEXT)
        del data["elecMtr"]["0702"]["04"]
        prom = cloud_message(MockMessage(json.dumps(data)))

        self.assertNotIn(
            "glowprom_consumption{type=\"electricity\",period=\"daily\"} "
            + "7.971", prom)
        self.assertIn(
            "glowprom_consumption{type=\"gas\",period=\"daily\"} 39.452", prom)

    def test_missing_gas(self):
        data = json.loads(MESSAGE_TEXT)
        del data["gasMtr"]["0702"]["0C"]
        prom = cloud_message(MockMessage(json.dumps(data)))

        self.assertIn(
            "glowprom_consumption{type=\"electricity\",period=\"daily\"} "
            + "7.971", prom)
        self.assertNotIn(
            "glowprom_consumption{type=\"gas\",period=\"daily\"} 39.452", prom)
