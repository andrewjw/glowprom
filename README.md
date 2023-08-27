# glowprom

[![Pipeline](https://github.com/andrewjw/glowprom/actions/workflows/build.yaml/badge.svg)](https://github.com/andrewjw/glowprom/actions/workflows/build.yaml)
[![PyPI version](https://badge.fury.io/py/glowprom.svg)](https://pypi.org/project/glowprom/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/glowprom)](https://pypi.org/project/glowprom/)
[![Docker Image Version (latest semver)](https://img.shields.io/docker/v/andrewjw/glowprom)](https://hub.docker.com/r/andrewjw/glowprom)
[![Docker Pulls](https://img.shields.io/docker/pulls/andrewjw/glowprom)](https://hub.docker.com/r/andrewjw/glowprom)
[![Coverage Status](https://coveralls.io/repos/github/andrewjw/glowprom/badge.svg?branch=master)](https://coveralls.io/github/andrewjw/glowprom?branch=master)

Receives gas and electric meter data from https://glowmarkt.com/ and exposes it to Prometheus.

```
usage: glowprom [-h] [--mqtt [MQTT]] [--port [PORT]] [--user [USER]] [--passwd [PASSWD]] [--topic [TOPIC]] [--bind [BIND]]

Listens to meter reports from Glow (glowmarkt.com) MQTT and exposes them as prometheus metrics

optional arguments:
  -h, --help         show this help message and exit
  --mqtt [MQTT]      the mqtt server to connect to. leave unset for the Glow cloud MQTT. (can also be set with $GLOWPROM_MQTT)
  --port [PORT]      the mqtt port to connect to. (can also be set with $GLOWPROM_MQTT_PORT)
  --user [USER]      the user name to use (can also be set with $GLOWPROM_USER)
  --passwd [PASSWD]  the password to use (can also be set with $GLOWPROM_PASSWD)
  --topic [TOPIC]    the topic to listen on for cloud MQTT (can also be set with $GLOWPROM_TOPIC)
  --bind [BIND]      the ip address and port to bind to
```

The Glow IHD can be used to connect a cloud MQTT server provided by Glow, or to your own local MQTT. These methods send different
messages, so different prometheus metrics are exposed depending on what you use.

# Cloud MQTT

```
# HELP consumption The consumption over the given period.
# TYPE consumption counter
glowprom_consumption{type="electricity",period="daily"} 4.761
glowprom_consumption{type="electricity",period="weekly"} 4.761
glowprom_consumption{type="electricity",period="monthly"} 61.483
glowprom_consumption{type="gas",period="daily"} 17.326
glowprom_consumption{type="gas",period="weekly"} 17.326
glowprom_consumption{type="gas",period="monthly"} 383.157
# HELP meter The meter reading.
# TYPE meter counter
glowprom_meter{type="electricity"} 15255.87
glowprom_meter{type="gas"} 5995.276
```

# Local MQTT
```
# HELP glowprom_timestamp The time the last update was received.
# TYPE glowprom_timestamp counter
glowprom_timestamp{type="electric", mpan="your_mpan"} 1667818379.0
glowprom_timestamp{type="gas", mprn="your_mprn"} 1667818361.0

# HELP glowprom_export_cumulative_Wh The total amount of energy exported.
# TYPE glowprom_export_cumulative_Wh counter
glowprom_export_cumulative_Wh{type="electric", mpan="your_mpan"} 0.0

# HELP glowprom_import_cumulative_Wh The total amount of energy imported.
# TYPE glowprom_import_cumulative_Wh counter
glowprom_import_cumulative_Wh{type="electric", mpan="your_mpan"} 15255822.0
glowprom_import_cumulative_Wh{type="gas", mprn="your_mprn"} 66589570.00000001

# HELP glowprom_import_day_Wh The amount of energy imported today.
# TYPE glowprom_import_day_Wh gauge
glowprom_import_day_Wh{type="electric", mpan="your_mpan"} 4714.0
glowprom_import_day_Wh{type="gas", mprn="your_mprn"} 17326.0

# HELP glowprom_import_week_Wh The amount of energy imported this week.
# TYPE glowprom_import_week_Wh gauge
glowprom_import_week_Wh{type="electric", mpan="your_mpan"} 4714.0
glowprom_import_week_Wh{type="gas", mprn="your_mprn"} 17326.0

# HELP glowprom_import_month_Wh The amount of energy imported this month.
# TYPE glowprom_import_month_Wh gauge
glowprom_import_month_Wh{type="electric", mpan="your_mpan"} 61436.0
glowprom_import_month_Wh{type="gas", mprn="your_mprn"} 383157.0

# HELP glowprom_import_price The current unit price for energy.
# TYPE glowprom_import_price gauge
glowprom_import_price{type="electric", mpan="your_mpan"} 0.16401
glowprom_import_price{type="gas", mprn="your_mprn"} 0.03623

# HELP glowprom_import_standing The standing charge for energy.
# TYPE glowprom_import_standing gauge
glowprom_import_standing{type="electric", mpan="your_mpan"} 0.19383
glowprom_import_standing{type="gas", mprn="your_mprn"} 0.168

# HELP glowprom_power_W The current amount of power being used.
# TYPE glowprom_power_W gauge
glowprom_power_W{type="electric", mpan="your_mpan"} 489.0

# HELP glowprom_import_cumulativevol_m3 The total volume of gas imported.
# TYPE glowprom_import_cumulativevol_m3 counter
glowprom_import_cumulativevol_m3{type="gas", mprn="your_mprn"} 5995.276

# HELP glowprom_import_dayvol_Wh The volume of gas imported today.
# TYPE glowprom_import_dayvol_Wh counter
glowprom_import_dayvol_Wh{type="gas", mprn="your_mprn"} 17326.0

# HELP glowprom_import_weekvol_Wh The volume of gas imported this week.
# TYPE glowprom_import_weekvol_Wh counter
glowprom_import_weekvol_Wh{type="gas", mprn="your_mprn"} 17326.0

# HELP glowprom_import_monthvol_Wh The volume of gas imported this month.
# TYPE glowprom_import_monthvol_Wh counter
glowprom_import_monthvol_Wh{type="gas", mprn="your_mprn"} 383157.0
```
