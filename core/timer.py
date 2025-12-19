def timer(searchCore, secs=0):
    from libs.imports import time
    if searchCore.is_alive():
        if secs < 20:
            time.sleep(1)
            secs += 1
            print(f"time searching:{secs}seconds")
            timer(searchCore, secs)
        else:
            return
    else:
        return