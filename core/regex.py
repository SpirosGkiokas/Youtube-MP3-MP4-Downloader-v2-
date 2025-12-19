from libs.imports import re

def isValid(url):    
    youtube_regex = re.compile(r'^(https?://)?(www\.)?(youtube\.com|youtu\.be)/.+$')
    print("YouTube match:", bool(youtube_regex.match(url)))
    return youtube_regex.match(url) is not None

def isRadio(url):
    radio_regex = re.compile(r'(?:/radio|[?&]list=RD|start_radio=1)')
    print("Radio match:", bool(radio_regex.match(url)))
    return radio_regex.search(url) is not None