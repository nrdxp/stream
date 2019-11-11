r"""Camera settings"""
import ffmpeg

INPUT_ARGS = {
    "s:v": "640X480",
}

OUTPUT_ARGS = {
    "c:v": "rawvideo",
    "pix_fmt": "yuv420p",
    "f": "sdl2"
}


def record_webcam(infile):
    """record webcam"""
    return (
        ffmpeg
        .input(infile, **INPUT_ARGS)
        .output("SDL output", **OUTPUT_ARGS)
        .global_args('-v', 'quiet')
        .run_async()
    )
