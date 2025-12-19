class downloadProgressWidgets():
    def __init__(self, app, settings, searchSettings):
        print("in progress")
        self.app = app
        self.settings = settings
        self.searchSettings = searchSettings

        self.createWidgets()


    def createWidgets(self):
        from libs.paths import imagePath
        from libs.imports import Image, ctk, mp
        from libs.styleSheet import colors
        from core.download import downloadWrapper
        from core.stop_download import stopDownload

        self.imageMedium = ctk.CTkImage(
            light_image=Image.open(imagePath),
            dark_image=Image.open(imagePath),
            size=(125, 125)
            )
        self.imageLarge = ctk.CTkImage(
            light_image=Image.open(imagePath),
            dark_image=Image.open(imagePath),
            size=(150, 150)
            )
        
        self.queue = mp.Queue()
        self.downloadCore = mp.Process(target=downloadWrapper, args=(self.searchSettings, self.queue))
        self.downloadCore.start()
        
        self.titleFrame = ctk.CTkFrame(self.app)
        self.titleFrame.configure(fg_color=colors['background'])
        self.imageLabel = ctk.CTkLabel(self.titleFrame, text="")
        self.titleLabel = ctk.CTkLabel(self.titleFrame, text="  Youtube MP3-MP4 Downloader")
        self.progressLabel = ctk.CTkLabel(self.app, text='\n\nStarting download')
        self.progressbar = ctk.CTkProgressBar(self.app, orientation="horizontal", corner_radius=0)
        self.progressbar.set(0)
        self.stopButton = ctk.CTkButton(self.app, text="Stop Download", command=lambda:stopDownload(self, self.app, self.settings, self.queue, self.downloadCore))

        self.styleWidgets()


    def styleWidgets(self):
        width = self.app.winfo_width()
        height = self.app.winfo_height()
        if width>=1000 and height>=900:
            self.prevSize = 'large'
            self.resize(self.prevSize)
        else:
            self.prevSize = 'medium'
            self.resize(self.prevSize)
        self.displayWidgets()


    def displayWidgets(self):
        from ui.set_progress import checkCore

        self.titleFrame.grid(row=0, column=0)
        self.imageLabel.pack(side="left")
        self.titleLabel.pack(side="right")
        self.progressLabel.grid(row=1, column=0)
        self.progressbar.grid(row=2, column=0)
        self.stopButton.grid(row=3, column=0)


        self.app.after(1000, lambda:checkCore(self, self.app, self.settings, self.queue, self.downloadCore))
        self.app.after(500, lambda:self.app.bind("<Configure>", self.onConfigure))


    def onConfigure(self, event):
        self.app.after_idle(self.checkSize)


    def checkSize(self):
        try:
            width = self.app.winfo_width()
            height = self.app.winfo_height()

            if width >= 1000 and height >= 900:
                size = 'large'
            elif width >= 800 and height >= 800:
                size = 'medium'
            if size != self.prevSize:
                self.prevSize = size
                self.resize(size)
        except Exception as e:
            print("Error in checkSize:", e)


    def resize(self, size):
        from libs.styleSheet import titleFont, labelFontDownload, buttonFont, buttonSize, pad_y, progressbarSize
        self.imageLabel.configure(image=self.imageMedium if size == "medium" else self.imageLarge)
        self.titleLabel.configure(font=titleFont[size], pady=pad_y[size]['titleLabel'])
        self.progressLabel.configure(font=labelFontDownload[size])
        self.progressLabel.grid_configure(pady=(pad_y[size]['progressLabel'],pad_y[size]['progressLabel']/2))
        self.progressbar.configure(width=progressbarSize[size]['width'], height=progressbarSize[size]['height'])
        self.stopButton.configure(font=buttonFont[size], width=buttonSize[size]['width'], height=buttonSize[size]['height'])
        self.stopButton.grid_configure(pady=pad_y[size]['stopButton'])