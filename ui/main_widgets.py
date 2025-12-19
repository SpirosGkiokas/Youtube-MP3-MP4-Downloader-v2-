from libs.imports import ctk

class mainWidgets:
    def __init__(self, app, settings):
        self.app = app
        self.settings = settings
        self.createWidgets()

    def createWidgets(self):
        from core.mode_controller import modeController
        from core.search_controller import searchController
        from libs.res_list import mp3List, mp4List
        from libs.paths import imagePath
        from libs.imports import Image
        from libs.styleSheet import colors
        
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

        self.enterUrlLabel = ctk.CTkLabel(self.app, text="Enter Url:")
        self.urlEntry = ctk.CTkEntry(self.app, placeholder_text="https://www.youtube.com/")

        self.modeCombobox = ctk.CTkComboBox(self.app, values=["MP3", "MP4"], state="readonly")
        self.modeCombobox.set(self.settings['mode'])
        self.modeCombobox.bind("<<ComboboxSelected>>", lambda e: modeController(self, self.settings, e))
        
        self.resCombobox = ctk.CTkComboBox(self.app, state="readonly")
        if self.settings['mode'] == "MP3":
            self.resCombobox.configure(values=mp3List)
            self.resCombobox.set(self.settings['lastMP3'])
        else:
            self.resCombobox.configure(values=mp4List)
            self.resCombobox.set(self.settings['lastMP4'])
        
        self.searchButton = ctk.CTkButton(self.app, text="Search",
                                          command=lambda:searchController(self, self.app, self.settings))

        modeController(self, self.app, self.settings)
        self.app.after(100, self.styleWidgets())


    def styleWidgets(self):
        width = self.app.winfo_width()
        height = self.app.winfo_height()
        if width<800 or height<800: 
            self.app.after(20, lambda:self.styleWidgets())
        else:
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
        self.enterUrlLabel.grid(row=1, column=0)
        self.urlEntry.grid(row=2, column=0)
        self.modeCombobox.grid(row=3, column=0)
        self.resCombobox.grid(row=4, column=0)
        self.searchButton.grid(row=5, column=0)
        self.app.after(500, lambda:self.app.bind("<Configure>", self.onConfigure))


    def onConfigure(self, event):
        self.app.after_idle(self.checkSize)


    def checkSize(self):
        width = self.app.winfo_width()
        height = self.app.winfo_height()
        if width >= 1000 and height >= 900:
            size = 'large'
        elif width >=800 and height >=800:
            size = 'medium'

        if size != self.prevSize:
            self.prevSize = size 
            self.resize(size)


    def resize(self, size):
        from libs.styleSheet import titleFont, labelFont, entryFont, entrySize, comboboxFont, comboboxSize, buttonFont, buttonSize, pad_y
        
        self.imageLabel.configure(image=self.imageMedium if size == "medium" else self.imageLarge)
        self.titleLabel.configure(font=titleFont[size], pady=pad_y[size]['titleLabel'])
        self.enterUrlLabel.configure(font=labelFont[size], pady=pad_y[size]['enterUrlLabel'])
        self.urlEntry.configure(font=entryFont[size], width=entrySize[size])
        self.modeCombobox.configure(font=comboboxFont[size], width=comboboxSize[size])
        self.modeCombobox.grid_configure(pady=pad_y[size]['modeCombobox'])
        self.resCombobox.configure(font=comboboxFont[size], width=comboboxSize[size])
        self.searchButton.configure(font=buttonFont[size], width=buttonSize[size]['width'], height=buttonSize[size]['height'])
        self.searchButton.grid_configure(pady=pad_y[size]['searchButton'])