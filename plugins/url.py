import os, asyncio, logging, random
from pyrogram import Client as app, filters

log = logging.getLogger(__name__)

class Utilities:
    async def run_subprocess(cmd):
        process = await asyncio.create_subprocess_exec(
            *cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
        )
        return await process.communicate()

    async def get_duration(file_link):
        ffmpeg_dur_cmd = [
            "ffprobe",
            "-headers",
            f"IAM:{Config.IAM_HEADER}",
            "-i",
            file_link,
            "-v",
            "error",
            "-show_entries",
            "format=duration",
            "-of",
            "csv=p=0:s=x",
            "-select_streams",
            "v:0",
        ]
        out, err = await Utilities.run_subprocess(ffmpeg_dur_cmd)
        log.debug(f"{out} \n {err}")
        out = out.decode().strip()
        if not out:
            return err.decode()
        duration = round(float(out))
        if duration:
            return duration
        return "No duration!"

    def is_url(text):
        return text.startswith("http")

@app.on_message(filters.private & filters.text)
async def url(client, message):
    if not Utilities.is_url(message.text):
        return
    await message.reply("Hi there, Please wait while I'm getting everything ready to process your request!")
