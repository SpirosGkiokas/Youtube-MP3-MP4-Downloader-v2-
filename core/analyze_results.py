def analyzeResults(self, app, settings, searchSettings, results):
    from ui.errors.not_found import notFound
    from ui.errors.res_not_found import resNotFound
    from ui.errors.res_check_error import resCheckError
    from ui.destroy_widgets import destroyWidgets
    from ui.download_widgets import downloadWidgets

    print("in analyze")
    print(results)

    if results != None:    
        match searchSettings['mode']:
            case "MP3":
                if results['audioQualities'] != None:
                    destroyWidgets(self, app)
                    downloadWidgets(app, settings, searchSettings, results)
                else:
                    resNotFound(self, app, settings, searchSettings)
            case "MP4":
                try:
                    res = int(searchSettings['quality'].strip('p'))
                    if res in results['videoResolutions']:
                        destroyWidgets(self, app)
                        downloadWidgets(app, settings, searchSettings, results)
                    else:
                        resNotFound(self, app, settings, searchSettings)
                except:
                    resCheckError(self, app, settings)
    else:
        notFound(self, app, settings, searchSettings)