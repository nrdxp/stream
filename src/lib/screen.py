r"""Screen settings"""
import ffmpeg


class SreenRecord:
    """Record the screen using kmsgrab"""

    def __init__(self, args):
        self.input_args = {
            "framerate": args.framerate,
            "f": "kmsgrab",
            "thread_queue_size": args.queue
        }

        self.audio_args = {
            "f": "alsa",
            "ac": 2,
            "thread_queue_size": args.queue
        }

        self.output_args = {
            "c:v": "h264_vaapi",
            "vf": "hwmap=derive_device=vaapi" +
                  ",scale_vaapi=w=1920:h=1080" +
                  ":format=nv12",
            "b:v": args.bitrate,
            "minrate:v": args.bitrate,
            "maxrate:v": args.bitrate,
            "bufsize:v": args.bitrate,
            "r:v": args.framerate,
            "g:v": args.framerate * 2,
            "pix_fmt": "vaapi_vld",
            "c:a": "aac",
            "ac": 2,
            "b:a": "96k",
            "bsf:a": "aac_adtstoasc"
        }

    def record_screen(self, infile, output):
        """record screen"""
        audio = ffmpeg.input("hw:0", **self.audio_args)
        return (
            ffmpeg
            .input(infile, **self.input_args)
            .output(audio, output, **self.output_args)
            .run_async()
        )
