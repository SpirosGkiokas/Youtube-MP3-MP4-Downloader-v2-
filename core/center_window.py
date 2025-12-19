def centerWindow(app, settings):
    screen_width =app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()
    x = ((screen_width-int(settings['windowSize']['width']))//2)
    y = ((screen_height-int(settings['windowSize']['height']))//2)
    app.geometry(f"{x}+{y}")