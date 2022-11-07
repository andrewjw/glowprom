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

import unittest
from unittest.mock import MagicMock, patch

from glowprom import connect


class Arguments:
    cloud = True
    mqtt = "cloudmqtt"
    port = 1883
    topic = "TestTopic"
    user = "TestUser"
    passwd = "TestPasswd"


def on_message(client, userdata, msg):
    print(str(msg.payload))


class TestMQTT(unittest.TestCase):
    @patch("paho.mqtt.client.Client", return_value=MagicMock())
    def test_connect(self, client):
        clientobj = client()

        connect(Arguments(), on_message, retry=False)

        self.assertTrue(clientobj.connect.called)

        clientobj.on_connect(clientobj, None, None, None)

        self.assertTrue(clientobj.subscribe.called)
