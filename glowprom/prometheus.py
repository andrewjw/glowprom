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

# Taken from https://gist.github.com/ndfred/b373eeafc4f5b0870c1b8857041289a9
# Fields gathered from the ZigBee Smart Energy Standard document
# 0702: Metering
# - 00: Reading Information Set
#   - 00: CurrentSummationDelivered: meter reading
#   - 01: CurrentSummationReceived
#   - 02: CurrentMaxDemandDelivered
#   - 07: ReadingSnapshotTime (UTC time)
#   - 14: Supply Status (enum): 0x2 is on
# - 02: Meter Status
#   - 00: Status (bit map): 10 means power quality event
# - 03: Formatting
#   - 00: UnitofMeasure (enum): 00 means kWh, 01 means m3
#   - 01: Multiplier
#   - 02: Divisor
#   - 03: SummationFormatting (bit map):
#         2B means 3 digits after the decimal point, 2 digits before.
#         FB means 3 digits after the decimal point, 16 digits before.
#         no leading zeros
#   - 04: DemandFormatting
#   - 06: MeteringDeviceType: 00 means Electric Metering,
#                             80 means Mirrored Gas Metering
#   - 07: SiteID: MPAN encoded in UTF-8
#   - 08: MeterSerialNumber (string)
#   - 12: AlternativeUnitofMeasure (enum)
# - 04: Historical Consumption
#   - 00: InstantaneousDemand (signed): current consumption
#   - 01: CurrentDayConsumptionDelivered
#   - 30: CurrentWeekConsumptionDelivered
#   - 40: CurrentMonthConsumptionDelivered
# - 0C: Alternative Historical Consumption
#   - 01: CurrentDayConsumptionDelivered
#   - 30: CurrentWeekConsumptionDelivered
#   - 40: CurrentMonthConsumptionDelivered
# 0705: Prepayment
# - 00: Prepayment Information Set
#   - 00: PaymentControlConfiguration (bit map)
#   - 01: CreditRemaining (signed)
# 0708: Device Management
# - 01: Supplier Control Attribute Set
#   - 01: ProviderName (string)


def prometheus(msg):
    # Code adapted from
    # https://gist.github.com/ndfred/b373eeafc4f5b0870c1b8857041289a9
    payload = json.loads(msg.payload)

    elecMtr = payload["elecMtr"]["0702"]

    elec_consumption = int(elecMtr["04"]["00"], 16)
    elec_daily_consumption = int(elecMtr["04"]["01"], 16)
    elec_weekly_consumption = int(elecMtr["04"]["30"], 16)
    elec_monthly_consumption = int(elecMtr["04"]["40"], 16)
    elec_multiplier = int(elecMtr["03"]["01"], 16)
    elec_divisor = float(int(elecMtr["03"]["02"], 16))
    elec_meter = int(elecMtr["00"]["00"], 16)

    gasMtr = payload["gasMtr"]["0702"]

    gas_daily_consumption = int(gasMtr["0C"]["01"], 16)
    gas_weekly_consumption = int(gasMtr["0C"]["30"], 16)
    gas_monthly_consumption = int(gasMtr["0C"]["40"], 16)
    gas_multiplier = int(gasMtr["03"]["01"], 16)
    gas_divisor = float(int(gasMtr["03"]["02"], 16))
    gas_meter = int(gasMtr["00"]["00"], 16)

    elec_daily_consumption = elec_daily_consumption * \
        elec_multiplier / elec_divisor
    elec_weekly_consumption = elec_weekly_consumption * \
        elec_multiplier / elec_divisor
    electricity_monthly_consumption = elec_monthly_consumption * \
        elec_multiplier / elec_divisor
    electricity_meter = elec_meter * elec_multiplier / elec_divisor
    gas_daily_consumption = gas_daily_consumption * \
        gas_multiplier / gas_divisor
    gas_weekly_consumption = gas_weekly_consumption * \
        gas_multiplier / gas_divisor
    gas_monthly_consumption = gas_monthly_consumption * \
        gas_multiplier / gas_divisor
    gas_meter = gas_meter * gas_multiplier / gas_divisor

    return f"""
consumption{{type='electricity',period='daily'}} {elec_daily_consumption}
consumption{{type='electricity',period='weekly'}} {elec_weekly_consumption}
consumption{{type='electricity',period='monthly'}} {elec_monthly_consumption}
meter{{type='electricity'}} {electricity_meter}
consumption{{type='gas',period='daily'}} {gas_daily_consumption}
consumption{{type='gas',period='weekly'}} {gas_weekly_consumption}
consumption{{type='gas',period='monthly'}} {gas_monthly_consumption}
meter{{type='gas'}} {gas_meter}
"""
