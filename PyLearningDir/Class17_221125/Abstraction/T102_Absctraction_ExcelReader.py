from abc import ABC, abstractmethod

class ExcelReader(ABC):

    @abstractmethod
    def read_from_excel(self):
        pass

class Browser(ExcelReader):

    @abstractmethod
    def open(self):
        pass

    def close(self):
        pass

class Testcase1(ExcelReader):

    def open(self):
        print("Open browser!")

    def close(self):
        print("Close the browser")

    def read_from_excel(self):
        print("Excel reader")

    def runTextcase1(self):
        print("Run The test case")
        self.open()
        self.read_from_excel()
        self.close()

tc = Testcase1()
tc.runTextcase1()


