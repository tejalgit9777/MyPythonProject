# Method Overriding

class BaseTest:
    def run(self):
        print("Running parent test")


class LoginTest(BaseTest):

    def run(self):
        print("Running child Test")


t = LoginTest()
#t1 = BaseTest()
t.run()