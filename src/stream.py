#!/usr/bin/env nix-shell
#! nix-shell -i python3 -p python38 python38Packages.ffmpeg-python ffmpeg_4
r"""This script with allow you to record your screen"""
from lib.args import PARSER
import lib.cam as cam
import lib.screen as screen


if __name__ == '__main__':
    ARGS = PARSER.parse_args()

    CAMSTREAM = cam.record_webcam(ARGS.camera)

    SCREEN_RECORDER = screen.SreenRecord(ARGS)
    SCREENSTREAM = SCREEN_RECORDER.record_screen("/dev/dri/card0", "out.mkv")

    CAMSTREAM.wait()
    SCREENSTREAM.wait()
