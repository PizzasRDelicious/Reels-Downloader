import yt_dlp


def download_instagram_reel(instagram_url, output_path):
    ydl_opts = {
        "outtmpl": output_path,
        "format": "mp4",
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([instagram_url])
        return True
    except Exception as e:
        print(f"Failed to download {instagram_url}: {e}")
        return False
