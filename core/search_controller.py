def searchController(self, app, settings):
    from core.regex import isValid, isRadio
    from core.settings import writeSettings
    from core.search import searchWrapper
    from core.timer import timer
    from libs.imports import th, mp
    from ui.errors.invalid_url import invalidUrl
    from ui.errors.radio_url import radioUrl

    print("In Search")#delete later
    searchSettings={
        "url": self.urlEntry.get(),
        "mode": self.modeCombobox.get(),
        "quality": self.resCombobox.get()
    }
    print(searchSettings)#delete later

    if searchSettings['url'].strip() == "":
        app.focus() #focus on app to get placeholder back
    else:
        settings[f'last{searchSettings['mode']}'] = searchSettings['quality']
        writeSettings(settings)
        self.urlEntry.delete(0, "end")
        self.urlEntry.configure(state="readonly")
        self.modeCombobox.configure(state="disabled")
        self.resCombobox.configure(state="disabled")
        self.searchButton.configure(command=None)

        if isValid(searchSettings['url']):
            if isRadio(searchSettings['url']):
                radioUrl(self, app, settings)
            else:
                print('valid url')
                self.urlEntry.configure(justify="center")

                queue = mp.Queue()

                searchCore = mp.Process(target=searchWrapper, args=(searchSettings, queue))
                searchCore.start()

                timerThread = th.Thread(target=timer, args=(searchCore, ))
                timerThread.start()

                waitSearch(self, app, settings, searchSettings, searchCore, timerThread, queue)
        else:
            invalidUrl(self, app, settings)

def waitSearch(self, app, settings, searchSettings, searchCore, timerThread, queue, dotCount=1):
    from core.analyze_results import analyzeResults
    from ui.errors.not_found import notFound

    if searchCore.is_alive() and timerThread.is_alive():
        self.urlEntry.configure(state="normal")
        self.urlEntry.delete(0, "end")
        self.urlEntry.insert(0, f"Searching{dotCount*'.'}")
        self.urlEntry.configure(state="readonly")
        if dotCount >= 3:
            dotCount = 1
        else: 
            dotCount+=1
        app.after(500, lambda:waitSearch(self, app, settings, searchSettings, searchCore, timerThread, queue, dotCount))
    elif searchCore.is_alive() and not timerThread.is_alive():
        searchCore.terminate()
        searchCore.join()
        notFound(self, app, settings, searchSettings)
    else:
        searchCore.join()
        results = queue.get()
        analyzeResults(self, app, settings, searchSettings, results)