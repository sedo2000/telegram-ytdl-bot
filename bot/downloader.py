import yt_dlp
import os
import uuid

DOWNLOAD_DIR = "/tmp"

def download_video(url, fmt):
    file_id = str(uuid.uuid4())
    ydl_opts = {
        "outtmpl": f"{DOWNLOAD_DIR}/{file_id}.%(ext)s",
        "format": fmt,
        "quiet": True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        ext = info["ext"]
        return f"{DOWNLOAD_DIR}/{file_id}.{ext}"
