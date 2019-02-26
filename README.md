# Toothbrush

Receive BLE packets from your Oral-B electrical toothbrush

## how to use

```
> toothbrush --help
Receive BLE packets from your Oral-B electrical toothbrush

Usage:
  toothbrush (-h | --help)
  toothbrush --version
  toothbrush [-v|-vv] [options] scan
  toothbrush [-v|-vv] [options] monitor <mac>

Options:
  -i <interface>        Bluetooth adapter interface
  -h --help             Show this message
  -v,-vv                Increase verbosity
  --version             Show version

> toothbrush scan
Oral-B Toothbrush 11:22:33:44:55:66
^C

> toothbrush monitor 11:22:33:44:55:66
{"running": 2, "pressure": 32, "time": 0, "mode": 7, "quadrant": 1}
{"running": 2, "pressure": 32, "time": 0, "mode": 7, "quadrant": 1}
{"running": 2, "pressure": 32, "time": 0, "mode": 7, "quadrant": 1}
{"running": 2, "pressure": 32, "time": 0, "mode": 7, "quadrant": 1}
{"running": 2, "pressure": 32, "time": 0, "mode": 7, "quadrant": 1}
{"running": 2, "pressure": 32, "time": 0, "mode": 7, "quadrant": 1}
^C

> toothbrush monitor 11:22:33:44:55:66 | mosquitto_pub -l -t /toothbrush

```

## credits
Inspired by https://github.com/rfaelens/domotica/blob/master/mqtt-toothbrush.py
