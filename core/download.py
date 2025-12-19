def download(searchSettings, queue):
    from libs.imports import os, ydl

    match searchSettings["mode"]:
        case "MP3":
            quality = int(searchSettings['quality'].strip("kbps"))
            download_options = {
                'format': 'bestaudio/best',
                'outtmpl': os.path.expanduser(f"~/Downloads") + "/%(title)s.%(ext)s",
                'postprocessors': [
                    {
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': quality
                    }
                ],
                'postprocessor_args': [
                    '-ar', '44100',
                    '-ac', '2'     
                ],
                'quiet': False,
                'progress_hooks': [progressHook(queue)]
            }
        case "MP4":
            resolution = int(searchSettings['quality'].strip("p"))
            download_options = {
                    "format": f"bestvideo[height<={resolution}]+bestaudio[acodec^=mp4a]/best[ext=mp4]",
                    'outtmpl': os.path.expanduser(f"~/Downloads") + "/%(title)s.%(ext)s",
                    "progress_hooks":  [progressHook(queue)]
                }
    try:
        with ydl.YoutubeDL(download_options) as d:
            d.download(searchSettings['url'])
    except Exception as e:
        print(e)
            
    
def progressHook(queue):
    cached_title = {"value": None}

    def hook(d):
        status = d.get("status")

        info = d.get("info_dict") or {}
        title = info.get("title")

        if title and not cached_title["value"]:
            cached_title["value"] = title

        if status == "finished":
            queue.put({
                "status": "Status: finished",
                "title": cached_title["value"] or "Unknown title",
                "percent": 1.0,
                "downloaded_mb": "",
                "total_mb": "",
                "eta": "Completed",
                "speed": "",
            })
            return

        downloaded = d.get("downloaded_bytes")
        total = d.get("total_bytes") or d.get("total_bytes_estimate")
        eta = d.get("eta")
        speed = d.get("speed")

        if any(v is None for v in (downloaded, total, eta, speed)):
            return

        percent = downloaded / total

        m, s = divmod(eta, 60)

        speed_formatted = (
            f"{speed / (1024 * 1024):.2f} MB/s"
            if speed >= 1024 * 1024
            else f"{speed / 1024:.1f} KB/s"
        )

        downloaded_mb = downloaded / (1024 * 1024)
        total_mb = total / (1024 * 1024)

        while not queue.empty():
            queue.get_nowait()

        queue.put({
            "status": f"Status: {status}",
            "title": cached_title["value"],
            "percent": percent,
            "downloaded_mb": f"{downloaded_mb:.2f}mb",
            "total_mb": f"{total_mb:.2f}mb",
            "eta": f"Time Remaining: {m}:{s:02d}",
            "speed": speed_formatted,
        })

    return hook

def downloadWrapper(searchSettings, queue):
    from core.av_cores import getNextAvailableCore
    from libs.imports import psutil
    
    core = getNextAvailableCore()
    p = psutil.Process()
    p.cpu_affinity([core])
    
    from core.search import search
    download(searchSettings, queue)
