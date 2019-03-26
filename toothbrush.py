# -*- mode: python; coding: utf-8 -*-

import logging

__version__ = "0.0.2"

_LOGGER = logging.getLogger(__name__)


def parse(device):
    mfd = device.get("ManufacturerData")

    if not mfd:
        _LOGGER.debug("no manufacturer data")
        return

    # 0xdc=220 is P&G
    # https://www.bluetooth.com/specifications/assigned-numbers/company-identifiers
    PG = 0xdc

    if PG not in mfd:
        _LOGGER.debug("wrong manufacturer key")
        return

    mfd = [int(x) for x in mfd[PG]]
    _LOGGER.debug("mfd: %s", mfd)

    # https://github.com/rfaelens/domotica/blob/master/mqtt-toothbrush.py
    return dict(
        # battery?
        running=mfd[3],
        pressure=mfd[4],
        time=mfd[5] * 60 + mfd[6],
        mode=mfd[7],
        quadrant=mfd[8],
    )
