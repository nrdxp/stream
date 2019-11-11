r"""Locally defined types
"""

import enum
import re
import argparse


def datasize(rate):
    """valid ffmpeg bitrate"""
    if not re.match("^[0-9]+[mk]{0,1}$", rate, re.IGNORECASE):
        raise argparse.ArgumentTypeError(
            f"'{rate}' is not a valid bitrate")
    return rate


STREAMS = enum.Enum("STREAMS", ("twitch", "youtube", "local"))


def streams(stream):
    """valid stream outputs"""
    try:
        return STREAMS[stream]
    except KeyError:
        raise argparse.ArgumentTypeError(
            f"'{stream}' is not a valid output stream")
