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
import time
import traceback
import sys

import paho.mqtt.client as mqtt


def on_connect(topic: str,
               client: mqtt.Client,
               userdata,
               flags,
               reason_code,
               properties):
    if reason_code != 0:
        sys.stderr.write(f"Failed to connect to mqtt: {reason_code}")
    else:
        print("Successfully connected to mqtt broker.")
        client.subscribe(topic)


def safe_on_message(on_message):
    def safe_on_message(client, userdata, msg):
        try:
            return on_message(client, userdata, msg)
        except Exception as e:
            sys.stderr.write(f"Exception processing message: {msg}\n")

            traceback.print_exc()

    return safe_on_message


def connect(args, on_message, retry=True):
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    client.on_connect = \
        functools.partial(on_connect,
                          args.topic if args.cloud else "glow/+/+/+")
    client.on_message = safe_on_message(on_message)

    client.username_pw_set(args.user, password=args.passwd)

    while True:
        try:
            client.connect(args.mqtt, args.port, 60)
        except Exception as e:  # pragma: no cover
            if not retry:
                raise
            print(e)
            time.sleep(10)
        else:
            break

    client.loop_forever()
