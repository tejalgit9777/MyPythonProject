a = 10 # variable everywhere in the program
class Test:
    b = 11 # Instance variable

    def test_info(self):
        a1 = 20 #     Local variable
        print(a1)
        print(self.b)
        print(a)

object_ref = Test()
object_ref.test_info()
