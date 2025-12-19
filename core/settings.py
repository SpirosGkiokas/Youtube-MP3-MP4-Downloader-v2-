def getSettings():
    from libs.paths import settingsPath
    from libs.imports import json
    from libs.res_list import mp3List, mp4List

    with open(settingsPath, "r") as readJSON:
        settings = json.load(readJSON)

    corruptedSettingFlag = False
    
    if settings['state'] != 'normal' and settings['state'] != 'zoomed': 
        settings['state']='normal' 
        corruptedSettingFlag=True

    if int(settings['windowSize']['width']) < 800:
        settings['windowSize']['width'] = 800
        corruptedSettingFlag=True

    if int(settings['windowSize']['height']) < 800:
        settings['windowSize']['height'] = 800
        corruptedSettingFlag=True

    if settings['mode'] not in ("MP3", "MP4"):
        settings['mode'] = "MP3"
        corruptedSettingFlag=True

    if settings['lastMP3'] not in mp3List: 
        settings['lastMP3']='192kbps'
        corruptedSettingFlag=True

    if settings['lastMP4'] not in mp4List: 
        settings['lastMP4']='720p'
        corruptedSettingFlag=True

    if corruptedSettingFlag:
        print('corrupted settings')
        writeSettings(settings)
    else:
        print('ok settings')

    return settings


def writeSettings(settings):
    from libs.paths import settingsPath
    from libs.imports import json, os

    with open(os.path.join(settingsPath), "w") as writeJSON:
            json.dump(settings, writeJSON, indent=4)