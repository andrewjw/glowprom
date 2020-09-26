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

import argparse
import os

from .exceptions import InvalidArguments

parser = argparse.ArgumentParser(
    description='Listens to meter reports from Glow (glowmarkt.com) MQTT and'
    + ' exposes them as prometheus metrics')
parser.add_argument('--user', type=str, nargs='?',
                    help='the user name to use (can also be set with '
                    + '$GLOWPROM_USER)')
parser.add_argument('--passwd', type=str, nargs='?',
                    help='the password to use (can also be set with '
                    + '$GLOWPROM_PASSWD)')
parser.add_argument('--topic', type=str, nargs='?',
                    help='the topic to listen on (can also be set with '
                    + '$GLOWPROM_TOPIC)')
parser.add_argument('--bind', type=str, nargs='?', default="0.0.0.0:9100",
                    help='the ip address and port to bind to')


def get_arguments(args):
    args = parser.parse_args(args)
    if "GLOWPROM_USER" in os.environ:
        args.user = os.environ["GLOWPROM_USER"]
    if "GLOWPROM_PASSWD" in os.environ:
        args.passwd = os.environ["GLOWPROM_PASSWD"]
    if "GLOWPROM_TOPIC" in os.environ:
        args.topic = os.environ["GLOWPROM_TOPIC"]

    if args.user is None:
        raise InvalidArguments("No username supplied. Either use --user "
                               + "or set $GLOWPROM_USER")
    if args.passwd is None:
        raise InvalidArguments("No password supplied. Either use --passwd "
                               + "or set $GLOWPROM_PASSWD")
    if args.topic is None:
        raise InvalidArguments("No topic supplied. Either use --topic "
                               + "or set $GLOWPROM_TOPIC")

    if ":" not in args.bind:
        args.bind = (args.bind, 9100)
    else:
        args.bind = (args.bind.split(":")[0], int(args.bind.split(":")[1]))

    return args
