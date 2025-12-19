def search(searchSettings, queue):
    from libs.imports import os, psutil, ydl

    options = {
        'quiet': True,
        'skip_download': True
    }  
    with ydl.YoutubeDL(options) as ydl:
        info = ydl.extract_info(searchSettings['url'], download=False)
        title = info.get('title', 'Unknown Title')
        thumbnail = info.get('thumbnail')
        formats = info.get('formats', [])
        videoResolutions = []
        audioQualities = []

        for f in formats:
            if f.get('vcodec') != 'none':
                res = f.get('height')
                if res:
                    videoResolutions.append(res)
            if f.get('acodec') != 'none':
                abr = f.get('abr')
                if abr:
                    audioQualities.append(abr)

        result = {
            'title': title,
            'thumbnail': thumbnail,
            'videoResolutions': sorted(set(videoResolutions)),
            'audioQualities': sorted(set(audioQualities))
        }

    queue.put(result)

def searchWrapper(searchSettings, queue):
    from core.av_cores import getNextAvailableCore
    from libs.imports import psutil
    
    core = getNextAvailableCore()
    p = psutil.Process()
    p.cpu_affinity([core])
    
    from core.search import search
    search(searchSettings, queue)