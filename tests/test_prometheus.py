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

import os
import unittest

from glowprom import prometheus


MESSAGE_TEXT = open("tests/test_message.txt", "rb").read()


class MockMessage:
    payload = MESSAGE_TEXT


class TestPrometheus(unittest.TestCase):
    def test_prometheus(self):
        prom = prometheus(MockMessage())

        self.assertIn(
            "consumption{type=\"electricity\",period=\"daily\"} 7.971", prom)
