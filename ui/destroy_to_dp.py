def destroyToDownloadProgress(self, app, settings, searchSettings):
    from ui.destroy_widgets import destroyWidgets
    from ui.download_progress_widgets import downloadProgressWidgets

    print("going to progress")
    destroyWidgets(self, app)
    if hasattr(self, "thumbnailMedium"):
        del self.thumbnailMedium
    if hasattr(self, "thumbnailLarge"):
        del self.thumbnailLarge
    downloadProgressWidgets(app, settings, searchSettings)