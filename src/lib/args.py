r""""Argument Parser
"""

import argparse
import pathlib
from lib.local import datasize, streams

PARSER = argparse.ArgumentParser()
PARSER.add_argument(
    "-r", "--framerate",
    help="set output framerate",
    type=int,
    default=60
)
PARSER.add_argument(
    "-b", "--bitrate",
    help="set ouput bitrate",
    default="4M",
    type=datasize
)
PARSER.add_argument(
    "-q", "--queue",
    help="set queue size for inputs",
    default="4M",
    type=datasize
)
PARSER.add_argument(
    "-c", "--camera",
    help="input camera device",
    default="/dev/video0",
    type=pathlib.Path
)
PARSER.add_argument(
    "-s", "--stream",
    help="service to stream to (twitch, youtube, local)",
    action='extend',
    nargs="+",
    default=[],
    type=streams
)
