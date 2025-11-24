# method is call directly by class name for static method

class Test:
    @staticmethod
    def test():
        print("Hello everyone!")

Test.test()