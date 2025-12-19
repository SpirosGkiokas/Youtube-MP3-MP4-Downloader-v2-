def notFound(self, app, settings, searchSettings):
    print('in not found url')
    self.urlEntry.configure(state="normal", justify="center")
    self.urlEntry.delete(0, "end")
    match searchSettings['mode']:
        case "MP3":
            self.urlEntry.insert(0, "Audio not found")
        case "MP4":
            self.urlEntry.insert(0, "Video not found")
    self.urlEntry.configure(state="readonly")
    app.after(2000, lambda:reset(self, app, settings))

def reset(self, app, settings):
    from core.search_controller import searchController

    print('in not found/reset')
    self.urlEntry.configure(state="normal", justify="left")
    self.urlEntry.delete(0, "end")
    app.focus()
    self.modeCombobox.configure(state="readonly")
    self.resCombobox.configure(state="readonly")
    self.searchButton.configure(command=lambda:searchController(self, app, settings))