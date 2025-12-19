def invalidUrl(self, app, settings):
    print('in invalid url')
    self.urlEntry.configure(state="normal", justify="center")
    self.urlEntry.insert(0, "Invalid Url")
    self.urlEntry.configure(state="readonly")
    app.after(2000, lambda:reset(self, app, settings))

def reset(self, app, settings):
    from core.search_controller import searchController

    print('in invalid url/reset')
    self.urlEntry.configure(state="normal", justify="left")
    self.urlEntry.delete(0, "end")
    app.focus()
    self.modeCombobox.configure(state="readonly")
    self.resCombobox.configure(state="readonly")
    self.searchButton.configure(command=lambda:searchController(self, app, settings))