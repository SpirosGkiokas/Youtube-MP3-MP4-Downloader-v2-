def goBack(self, app, settings):
    from ui.destroy_widgets import destroyWidgets
    from ui.main_widgets import mainWidgets

    print("going back")
    destroyWidgets(self, app)
    if hasattr(self, "thumbnailMedium"):
        del self.thumbnailMedium
    if hasattr(self, "thumbnailLarge"):
        del self.thumbnailLarge
    mainWidgets(app, settings)