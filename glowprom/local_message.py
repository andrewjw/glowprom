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

import datetime
import json

# {'electricitymeter': {'timestamp': '2022-11-07T09:20:08Z',
#   'energy': {'export': {'cumulative': 0.0, 'units': 'kWh'},
#              'import': {'cumulative': 15254.827, 'day': 3.717,
#                         'week': 3.717, 'month': 60.439, 'units': 'kWh',
#                         'mpan': 'abcd', 'supplier': 'Octopus Energy',
#                         'price': {'unitrate': 0.16401,
#                                   'standingcharge': 0.19383}}},
#   'power': {'value': 0.425, 'units': 'kW'}}}

# {'gasmeter': {'timestamp': '2022-11-07T09:35:38Z',
#   'energy': {'import': {'cumulative': 66589.57, 'day': 17.326,
#                         'week': 17.326, 'month': 383.157, 'units': 'kWh',
#                         'cumulativevol': 5995.276,
#                         'cumulativevolunits': 'm3',
#                         'dayvol': 17.326, 'weekvol': 17.326,
#                         'monthvol': 383.157,
#                         'dayweekmonthvolunits': 'kWh',
#                         'mprn': 'wxyz',
#                         'supplier': '---',
#                         'price': {'unitrate': 0.03623,
#                                   'standingcharge': 0.168}}}}}

# {'timestamp': '2026-01-19T20:55:38Z', 'software': 'v2.0.2',
# 'hardware': 'GLOW-IHD-02-1v4-SMETS2', 'wifistamac': 'BCDDC2C6A91C',
# 'smetsversion': 'SMETS2', 'eui': '70:B3:D5:21:E0:00:8D:10',
# 'zigbee': '1.2.5', 'han': {'rssi': -88, 'status': 'joined', 'lqi': 48}}

METRIC = "glowprom_{metric}"
METRIC_KEYS = '{{type="{type}", {idname}="{idvalue}"}}'

METRIC_METADATA = {
    "timestamp": ("The time the last update was received.", "counter", False),
    "export_cumulative": ("The total amount of energy exported.", "counter", True),
    "import_cumulative": ("The total amount of energy imported.", "counter", True),
    "import_day": ("The amount of energy imported today.", "gauge", True),
    "import_week": ("The amount of energy imported this week.", "gauge", True),
    "import_month": ("The amount of energy imported this month.", "gauge", True),
    "import_price": ("The current unit price for energy.", "gauge", False),
    "import_standing": ("The standing charge for energy.", "gauge", False),
    "power": ("The current amount of power being used.", "gauge", True),
    "import_cumulativevol": ("The total volume of gas imported.", "counter", True),
    "import_dayvol": ("The volume of gas imported today.", "counter", True),
    "import_weekvol": ("The volume of gas imported this week.", "counter", True),
    "import_monthvol": ("The volume of gas imported this month.", "counter", True),
}

METRIC_HELP = "# HELP {metric} {help}"
METRIC_TYPE = "# TYPE {metric} {type}"

ELECTRIC_DATA = {}
GAS_DATA = {}
STATE_TIMESTAMP = None
VERSIONS = {}
RSSI = None
LQI = None


def local_message(msg):
    # # Code adapted from
    # # https://gist.github.com/ndfred/b373eeafc4f5b0870c1b8857041289a9
    payload = json.loads(msg.payload)

    if "electricitymeter" in payload:
        energy = payload["electricitymeter"]["energy"]

        mpan = energy["import"]["mpan"]
        if mpan.lower() == "read pending":  # pragma: no cover
            return
        if mpan not in ELECTRIC_DATA:
            ELECTRIC_DATA[mpan] = {}
        ELECTRIC_DATA[mpan]["timestamp"] = datetime.datetime.strptime(
            payload["electricitymeter"]["timestamp"], r"%Y-%m-%dT%H:%M:%SZ"
        ).timestamp()
        ELECTRIC_DATA[mpan]["export_cumulative"] = convert_units(
            energy["export"]["cumulative"], energy["export"]["units"]
        )
        ELECTRIC_DATA[mpan]["import_cumulative"] = convert_units(
            energy["import"]["cumulative"], energy["import"]["units"]
        )
        ELECTRIC_DATA[mpan]["import_day"] = convert_units(
            energy["import"]["day"], energy["import"]["units"]
        )
        ELECTRIC_DATA[mpan]["import_week"] = convert_units(
            energy["import"]["week"], energy["import"]["units"]
        )
        ELECTRIC_DATA[mpan]["import_month"] = convert_units(
            energy["import"]["month"], energy["import"]["units"]
        )
        ELECTRIC_DATA[mpan]["import_price"] = energy["import"]["price"]["unitrate"]
        ELECTRIC_DATA[mpan]["import_standing"] = energy["import"]["price"][
            "standingcharge"
        ]
        ELECTRIC_DATA[mpan]["power"] = convert_units(
            payload["electricitymeter"]["power"]["value"],
            payload["electricitymeter"]["power"]["units"],
        )

    elif "gasmeter" in payload:
        energy = payload["gasmeter"]["energy"]
        mprn = energy["import"]["mprn"]
        if mprn.lower() == "read pending":  # pragma: no cover
            return
        if mprn not in GAS_DATA:
            GAS_DATA[mprn] = {}
        GAS_DATA[mprn]["timestamp"] = datetime.datetime.strptime(
            payload["gasmeter"]["timestamp"], r"%Y-%m-%dT%H:%M:%SZ"
        ).timestamp()
        GAS_DATA[mprn]["import_cumulative"] = convert_units(
            energy["import"]["cumulative"], energy["import"]["units"]
        )
        GAS_DATA[mprn]["import_day"] = convert_units(
            energy["import"]["day"], energy["import"]["units"]
        )
        GAS_DATA[mprn]["import_week"] = convert_units(
            energy["import"]["week"], energy["import"]["units"]
        )
        GAS_DATA[mprn]["import_month"] = convert_units(
            energy["import"]["month"], energy["import"]["units"]
        )
        GAS_DATA[mprn]["import_cumulativevol"] = convert_units(
            energy["import"]["cumulativevol"], energy["import"]["cumulativevolunits"]
        )
        GAS_DATA[mprn]["import_dayvol"] = convert_units(
            energy["import"]["dayvol"], energy["import"]["dayweekmonthvolunits"]
        )
        GAS_DATA[mprn]["import_weekvol"] = convert_units(
            energy["import"]["weekvol"], energy["import"]["dayweekmonthvolunits"]
        )
        GAS_DATA[mprn]["import_monthvol"] = convert_units(
            energy["import"]["monthvol"], energy["import"]["dayweekmonthvolunits"]
        )
        GAS_DATA[mprn]["import_price"] = energy["import"]["price"]["unitrate"]
        GAS_DATA[mprn]["import_standing"] = energy["import"]["price"]["standingcharge"]
    elif "han" in payload:
        global RSSI, LQI, STATE_TIMESTAMP
        STATE_TIMESTAMP = datetime.datetime.strptime(
            payload["timestamp"], r"%Y-%m-%dT%H:%M:%SZ"
        ).timestamp()
        VERSIONS["software"] = payload["software"]
        VERSIONS["hardware"] = payload["hardware"]
        VERSIONS["smetsversion"] = payload["smetsversion"]
        VERSIONS["zigbee"] = payload["zigbee"]
        RSSI = payload["han"]["rssi"]
        LQI = payload["han"]["lqi"]
    else:  # pragma: no cover
        print(f"Unknown payload type {key}")

    lines = []
    for metric in METRIC_METADATA.keys():
        help, metric_type, has_units = METRIC_METADATA[metric]

        if has_units:
            for unit in get_units_for_metric(metric):
                metric_name = METRIC.format(metric=metric) + "_" + unit
                lines.append(METRIC_HELP.format(metric=metric_name, help=help))
                lines.append(METRIC_TYPE.format(metric=metric_name, type=metric_type))
        else:
            metric_name = METRIC.format(metric=metric)
            lines.append(METRIC_HELP.format(metric=metric_name, help=help))
            lines.append(METRIC_TYPE.format(metric=metric_name, type=metric_type))

        for mpan in ELECTRIC_DATA:
            if metric in ELECTRIC_DATA[mpan]:
                if has_units:
                    value = ELECTRIC_DATA[mpan][metric][0]
                    metric_name = (
                        METRIC.format(metric=metric)
                        + "_"
                        + ELECTRIC_DATA[mpan][metric][1]
                    )
                else:
                    value = ELECTRIC_DATA[mpan][metric]
                    metric_name = METRIC.format(metric=metric)

                keys = METRIC_KEYS.format(type="electric", idname="mpan", idvalue=mpan)
                lines.append(f"{metric_name}{keys} {value}")

        for mprn in GAS_DATA:
            if metric in GAS_DATA[mprn]:
                if has_units:
                    value = GAS_DATA[mprn][metric][0]
                    metric_name = (
                        METRIC.format(metric=metric) + "_" + GAS_DATA[mprn][metric][1]
                    )
                else:
                    value = GAS_DATA[mprn][metric]
                    metric_name = METRIC.format(metric=metric)

                keys = METRIC_KEYS.format(type="gas", idname="mprn", idvalue=mprn)
                lines.append(f"{metric_name}{keys} {value}")

        lines.append("")

    if STATE_TIMESTAMP is not None:
        lines.append(
            f"{METRIC.format(metric='timestamp')}{{type=\"state\"}} {STATE_TIMESTAMP}\n"
        )
    if len(VERSIONS) > 0:
        lines.append(
            METRIC_HELP.format(
                metric=METRIC.format(metric="versions"),
                help="The software and hardware versions of the IHD.",
            )
        )
        lines.append(
            METRIC_TYPE.format(
                metric=METRIC.format(metric="versions"),
                type="gauge",
            )
        )
        lines.append(
            METRIC.format(metric="versions")
            + "{"
            + ",".join(f'{k}="{v}"' for k, v in VERSIONS.items())
            + "} 1\n"
        )
    if RSSI is not None:
        lines.append(
            METRIC_HELP.format(
                metric=METRIC.format(metric="rssi"),
                help="The RSSI of the HAN connection.",
            )
        )
        lines.append(
            METRIC_TYPE.format(
                metric=METRIC.format(metric="rssi"),
                type="gauge",
            )
        )
        lines.append(f"{METRIC.format(metric='rssi')} {RSSI}\n")
    if LQI is not None:
        lines.append(
            METRIC_HELP.format(
                metric=METRIC.format(metric="lqi"),
                help="The LQI of the HAN connection (0 min, 255 best).",
            )
        )
        lines.append(
            METRIC_TYPE.format(
                metric=METRIC.format(metric="lqi"),
                type="gauge",
            )
        )
        lines.append(f"{METRIC.format(metric='lqi')} {LQI}\n")

    return "\n".join(lines)


def get_units_for_metric(metric):
    units = set()
    for mpan in ELECTRIC_DATA.keys():
        if metric in ELECTRIC_DATA[mpan]:
            units.add(ELECTRIC_DATA[mpan][metric][1])
    for mprn in GAS_DATA.keys():
        if metric in GAS_DATA[mprn]:
            units.add(GAS_DATA[mprn][metric][1])
    return units


def convert_units(value, units):
    if units == "kW":
        return (value * 1000, "W")
    if units == "kWh":
        return (value * 1000, "Wh")
    return (value, units)
