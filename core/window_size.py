def windowSize(app, settings):
    from core.settings import writeSettings

    width = app.winfo_width()
    height = app.winfo_height()
    if app.state() == "zoomed":
        settings['state'] = "zoomed"
        writeSettings(settings)
    else:
        settings['state'] = "normal"
        if width >= 700 and height >= 700:
            if int(settings['windowSize']['width']) != width or int(settings['windowSize']['height']) != height:
                settings['windowSize']['width'] = width
                settings['windowSize']['height'] = height
        writeSettings(settings)

    app.after(2000, lambda:windowSize(app, settings))