def safeFilename(name):
    from libs.imports import re
    return re.sub(r'[\\/:*?"<>|]', '_', name)