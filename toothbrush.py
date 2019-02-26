# -*- mode: python; coding: utf-8 -*-

import logging
import asyncio
from time import time
from json import dumps as to_json
from sys import stderr
from collections import OrderedDict
from datetime import timezone
import subprocess
import json
import blus

__version__ = "0.0.1"

_LOGGER = logging.getLogger(__name__)


def parse(device):
    mfd = device.get("ManufacturerData")
    # 220 is Procter & Gamble
    # https://www.bluetooth.com/specifications/assigned-numbers/company-identifiers
    PG = 0x00DC
    if not mfd:
        _LOGGER.debug("no manufacturer data")
        return

    if PG not in mfd:
        _LOGGER.debug("wrong manufacturer key")
        return

    mfd = [int(x) for x in mfd[PG]]
    _LOGGER.debug("mfd: %s", mfd)

    return dict(
        running=mfd[3],
        pressure=mfd[4],
        time=mfd[5] * 60 + mfd[6],
        mode=mfd[7],
        quadrant=mfd[8],
    )
