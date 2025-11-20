#Build a Test Framework with Encapsulation + Inheritance
class BaseClass:
    _driver = "Chrome"

    def setup(self):
        print("Launching driver",self._driver)

    def teardown(self):
        print("Closing driver")

class LoginTest(BaseClass):

    def runtest(self):
        self.setup()

        __username = str(input("Enter your username: ").strip())
        __password = str(input("Enter your password: ").strip())
        if __username == "Teju" and __password == "shine":
            print("Running login with test username: ",__username)
        else:
            print("Invalid Credential!!")

        self.teardown()

login = LoginTest()
login.runtest()

