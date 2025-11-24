class ExcelReader:

    @staticmethod
    def readExcelFile():
        print("Reading from Excel")
class MYSQLDB:

    @staticmethod
    def readMySQLFile():
        print("Reading from MySQL")

class TC1:

    def run_testcase(self):
        ExcelReader.readExcelFile()
        MYSQLDB.readMySQLFile()
        print("Hello")

class TC2:

    def run_testcase(self):
        ExcelReader.readExcelFile()
        MYSQLDB.readMySQLFile()
        print("Hello")

tc1 = TC1()
tc2 = TC1()
tc1.run_testcase()
tc2.run_testcase()