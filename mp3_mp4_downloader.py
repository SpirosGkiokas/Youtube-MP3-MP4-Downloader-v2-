def createApp(settings):
    from core.center_window import centerWindow
    from core.taskbar import setTaskbarIcon
    from core.window_size import windowSize
    from libs.imports import ctk
    from libs.paths import iconPath
    from ui.main_widgets import mainWidgets

    app = ctk.CTk()
    app.title("Youtube MP3-MP4 Downloader")
    app.minsize(800,800)
    app.iconbitmap(iconPath)
    app.columnconfigure(0, weight=1)
    

    if settings['state'] == "zoomed":
        app.after(0, lambda:app.state("zoomed"))
    else:
        app.geometry(f"{settings['windowSize']['width']}x{settings['windowSize']['height']}")

    centerWindow(app, settings)
    setTaskbarIcon()
    app.after(100, lambda:windowSize(app, settings))

    mainWidgets(app, settings)

    app.mainloop()

if __name__ == "__main__":
    from core.settings import getSettings
    import sys

    MIN_PYTHON = (3, 12)

    if sys.version_info < MIN_PYTHON:
        sys.exit(
            f"This project requires Python {MIN_PYTHON[0]}.{MIN_PYTHON[1]} or newer. "
            f"You are using {sys.version_info.major}.{sys.version_info.minor}."
        )

    settings = getSettings()
    print(settings)
    createApp(settings)