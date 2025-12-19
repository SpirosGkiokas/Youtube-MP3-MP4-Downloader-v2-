def destroyWidgets(self, app):
        for widget in app.winfo_children():
            widget.destroy()
        app.unbind("<Configure>")