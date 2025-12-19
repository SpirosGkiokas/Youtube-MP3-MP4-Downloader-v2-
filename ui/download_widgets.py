class downloadWidgets():
    def __init__(self, app, settings, searchSettings, results):
        from libs.imports import requests, BytesIO, Image, ctk
        print("in download")
        self.app = app
        self.settings = settings
        self.searchSettings = searchSettings
        self.results = results

        thumbnailRequest = requests.get(self.results['thumbnail'])
        thumbnailData = thumbnailRequest.content
        thumbnail = Image.open(BytesIO(thumbnailData))
        self.thumbnailMedium = ctk.CTkImage(thumbnail, size=(300, 168))
        self.thumbnailLarge = ctk.CTkImage(thumbnail, size=(400, 225))

        self.createWidgets()


    def createWidgets(self):
        from libs.paths import imagePath
        from libs.imports import Image, ctk
        from libs.styleSheet import colors
        from ui.go_back import goBack
        from ui.destroy_to_dp import destroyToDownloadProgress

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
        
        self.titleFrame = ctk.CTkFrame(self.app)
        self.titleFrame.configure(fg_color=colors['background'])
        self.imageLabel = ctk.CTkLabel(self.titleFrame, text="")
        self.titleLabel = ctk.CTkLabel(self.titleFrame, text="  Youtube MP3-MP4 Downloader")
        self.thumbnailLabel = ctk.CTkLabel(self.app, text="")
        self.videoTitleLabel = ctk.CTkLabel(self.app, text=(f"Title:\n{self.results['title']}"))
        self.downloadButton = ctk.CTkButton(self.app, text="Download", command=lambda:destroyToDownloadProgress(self, self.app, self.settings, self.searchSettings))
        self.goBackButton = ctk.CTkButton(self.app, text="Go Back", command=lambda:goBack(self, self.app, self.settings))

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
        self.titleFrame.grid(row=0, column=0)
        self.imageLabel.pack(side="left")
        self.titleLabel.pack(side="right")
        self.thumbnailLabel.grid(row=1, column=0)
        self.videoTitleLabel.grid(row=2, column=0)
        self.downloadButton.grid(row=3, column=0)
        self.goBackButton.grid(row=4, column=0)
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
        from libs.styleSheet import titleFont, labelFontDownload, buttonFont, buttonSize, pad_y
    
        self.imageLabel.configure(image=self.imageMedium if size == "medium" else self.imageLarge)
        self.titleLabel.configure(font=titleFont[size], pady=pad_y[size]['titleLabel'])
        self.thumbnailLabel.configure(image=self.thumbnailLarge)
        self.thumbnailLabel.grid_configure(pady=(pad_y[size]['thumbnail'],0))
        self.videoTitleLabel.configure(font=labelFontDownload[size])
        self.videoTitleLabel.grid_configure(pady=(pad_y[size]['videoTitleLabel'],0))
        self.downloadButton.configure(font=buttonFont[size], width=buttonSize[size]['width'], height=buttonSize[size]['height'])
        self.downloadButton.grid_configure(pady=pad_y[size]['searchButton'])
        self.goBackButton.configure(font=buttonFont[size], width=buttonSize[size]['width'], height=buttonSize[size]['height'])