import os

dirPath = os.getcwd()
corePath = os.path.join(dirPath, "core")
libsPath = os.path.join(dirPath, "libs")
resourcesPath = os.path.join(dirPath, "resources")
uiPath = os.path.join(dirPath, "ui")
iconPath = os.path.join(resourcesPath, "icon", "mp3-mp4-downloader-icon.ico")
imagePath = os.path.join(resourcesPath, "images", "mp3-mp4-downloader-icon.png")
settingsPath = os.path.join(resourcesPath, "settings.json")
ffmpegPath = os.path.join(libsPath, "ffmpeg", "bin")

# Inject into environment PATH
os.environ["PATH"] = ffmpegPath + os.pathsep + os.environ["PATH"]