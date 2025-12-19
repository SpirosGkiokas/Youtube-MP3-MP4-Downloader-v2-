import ctypes as ct

def setTaskbarIcon():
    #taskbar icon
    myappid = 'MP3-MP4 Youtube Downloader' 
    ct.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)