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

import io
import json
from datetime import datetime, timedelta
import unittest

from glowprom.server import Handler, update_stats

MESSAGE_TEXT = open("tests/test_message.txt", "rb").read()


class MockMessage:
    payload = MESSAGE_TEXT


class MockHandler(Handler):
    def __init__(self):
        self.wfile = io.BytesIO()
        self.requestline = "GET"
        self.client_address = ("127.0.0.1", 8000)
        self.request_version = "1.0"
        self.command = "GET"


class TestServer(unittest.TestCase):
    def setUp(self):
        update_stats(True)(None, None, None)

    def test_index(self):
        handler = MockHandler()
        handler.path = "/"
        handler.do_GET()

        handler.wfile.seek(0)
        self.assertTrue("/metrics" in handler.wfile.read().decode("utf8"))

    def test_error(self):
        handler = MockHandler()
        handler.path = "/error"
        handler.do_GET()

        handler.wfile.seek(0)
        self.assertTrue("404" in handler.wfile.read().decode("utf8"))

    def test_metrics(self):
        update_stats(True)(None, None, MockMessage())

        handler = MockHandler()
        handler.path = "/metrics"
        handler.do_GET()

        handler.wfile.seek(0)
        self.assertTrue(
            "consumption" in handler.wfile.read().decode("utf8"))

    def test_metrics_before_update(self):
        handler = MockHandler()
        handler.path = "/metrics"
        handler.do_GET()

        handler.wfile.seek(0)
        self.assertTrue("404" in handler.wfile.read().decode("utf8"))
