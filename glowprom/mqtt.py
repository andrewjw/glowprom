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

import functools

import paho.mqtt.client as mqtt


def on_connect(topic, client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    client.subscribe(topic)


def connect(args, on_message):
    client = mqtt.Client()
    client.on_connect = functools.partial(on_connect, args.topic)
    client.on_message = on_message

    client.username_pw_set(args.user, password=args.passwd)
    client.connect("glowmqtt.energyhive.com", 1883, 60)

    client.loop_forever()
