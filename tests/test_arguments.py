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

from glowprom import get_arguments, InvalidArguments


class TestArguments(unittest.TestCase):
    def setUp(self):
        os.environ = {}

    def test_user_environ(self):
        os.environ["GLOWPROM_USER"] = "testuser"
        args = get_arguments(["--passwd", "testpassword", "--topic", "topic"])
        self.assertEqual("testuser", args.user)
        self.assertEqual("testpassword", args.passwd)

    def test_passwd_environ(self):
        os.environ["GLOWPROM_PASSWD"] = "testpassword"
        args = get_arguments(["--user", "testuser", "--topic", "topic"])
        self.assertEqual("testpassword", args.passwd)

    def test_passwd_environ(self):
        os.environ["GLOWPROM_TOPIC"] = "topic"
        args = get_arguments(["--user", "testuser",
                              "--passwd", "testpassword"])
        self.assertEqual("topic", args.topic)

    def test_bind_without_port(self):
        os.environ["GLOWPROM_USER"] = "testuser"
        os.environ["GLOWPROM_PASSWD"] = "testpassword"
        os.environ["GLOWPROM_TOPIC"] = "topic"
        args = get_arguments(["--bind", "192.168.1.2"])
        self.assertEqual("192.168.1.2", args.bind[0])
        self.assertEqual(9100, args.bind[1])

    def test_no_user(self):
        os.environ["GLOWPROM_PASSWD"] = "testpasswd"
        os.environ["GLOWPROM_TOPIC"] = "topic"
        self.assertRaises(InvalidArguments, get_arguments, [])

    def test_no_passwd(self):
        os.environ["GLOWPROM_USER"] = "testuser"
        os.environ["GLOWPROM_TOPIC"] = "topic"
        self.assertRaises(InvalidArguments, get_arguments, [])

    def test_no_topic(self):
        os.environ["GLOWPROM_USER"] = "testuser"
        os.environ["GLOWPROM_PASSWD"] = "testpasswd"
        self.assertRaises(InvalidArguments, get_arguments, [])
