def modeController(self, app, settings):
    from libs.res_list import mp3List, mp4List
    from core.settings import writeSettings

    try:
        mode = self.modeCombobox.get()
        if settings['mode'] != mode:
            match mode:
                case "MP3":
                    self.resCombobox.configure(values=mp3List)
                    self.resCombobox.set(settings['lastMP3'])
                case "MP4":
                    self.resCombobox.configure(values=mp4List)
                    self.resCombobox.set(settings['lastMP4'])
            settings['mode'] = mode
            writeSettings(settings)
        app.after(200, lambda:modeController(self, app, settings))
    except:
        return