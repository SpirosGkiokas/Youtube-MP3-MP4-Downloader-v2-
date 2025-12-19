def stopDownload(self, app, settings, queue, downloadCore):
    from core.safe_filename import safeFilename
    from libs.imports import os, glob, messagebox
    from ui.main_widgets import mainWidgets
    from ui.destroy_widgets import destroyWidgets

    try:
        data = queue.get_nowait()
        title = data['title']
        safeTitle = safeFilename(title)
        downloadDir = os.path.expanduser("~/Downloads")


        if downloadCore.is_alive():
            downloadCore.terminate()
            downloadCore.join()  

        pattern = os.path.join(downloadDir, "*.part")
        for partFile in glob.glob(pattern):
            if os.path.basename(partFile).startswith(safeTitle) or os.path.basename(partFile).startswith(title):
                os.remove(partFile)
                print(f"Deleted partial file: {partFile}")

        extensions = ["mp4", "mp3", "webm"]
        for ext in extensions:
            pattern = os.path.join(downloadDir, f"{safeTitle}*.{ext}")
            for filePath in glob.glob(pattern):
                os.remove(filePath)
                print(f"Deleted final file: {filePath}")

        destroyWidgets(self, app)
        mainWidgets(app, settings)
        messagebox.showinfo("Download Stopped", "Download Stopped. Deleted partial files.")

    except Exception:
        app.after(100, lambda: stopDownload(self, app, settings, queue, downloadCore))
