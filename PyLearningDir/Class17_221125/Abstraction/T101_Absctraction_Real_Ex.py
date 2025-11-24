from abc import ABC, abstractmethod

class BrowserManager(ABC):

    @abstractmethod
    def open(self):
        pass

    def close(self):
        print("Close the browser")

class ChromeBrowserManager(BrowserManager):

    def open(self):
        print("Open chrome browser!")

cbm=ChromeBrowserManager()
cbm.open()
cbm.close()

