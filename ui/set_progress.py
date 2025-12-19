def checkCore(self, app, settings, queue, downloadCore):
    if downloadCore.is_alive():
        getProgress(self, app, settings, queue, downloadCore)
    else:
        pass #show finish screens

def getProgress(self, app, settings, queue, downloadCore):
    try:
        if not queue.empty():
            data = queue.get()
            print(data)
            setProgress(self, app, settings, queue, downloadCore, data)
        else:
            app.after(500, lambda:checkCore(self, app, settings, queue, downloadCore))
    except:
        app.after(500, lambda:checkCore(self, app, settings, queue, downloadCore))

def setProgress(self, app, settings, queue, downloadCore, data):
    from libs.imports import os, messagebox
    from core.safe_filename import safeFilename
    from ui.destroy_widgets import destroyWidgets
    from ui.main_widgets import mainWidgets

    if data['status'] != "Status: finished":
        self.progressLabel.configure(text=f"{data['status']}\n{data['eta']}\n{data['downloaded_mb']}/{data['total_mb']}({data['speed']})")
        self.progressbar.set(data['percent'])
        app.after(500, lambda: checkCore(self, app, settings, queue, downloadCore))

    else:
        safeTitle = safeFilename(data['title'])
        downloadDir = os.path.expanduser("~/Downloads")
        filepathMP3 = os.path.join(downloadDir, f"{safeTitle}.mp3")
        filepathMP4 = os.path.join(downloadDir, f"{safeTitle}.mp4")
        filepathWebm = os.path.join(downloadDir, f"{safeTitle}.webm")

        paths = (filepathMP3, filepathMP4, filepathWebm)

        if any(os.path.exists(path) for path in paths):
            destroyWidgets(self, app)
            mainWidgets(app, settings)
            messagebox.showinfo("Download Finished", "File Location At Download Folder")
        else:
            self.progressLabel.configure(text="\n\nMerging")
            app.after(500, lambda: setProgress(self, app, settings, queue, downloadCore, data))