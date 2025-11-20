# Multilevel Inheritance

class Requirement:

    def requirement1(self):
        print("Step 1 Requirement 1")

class Development(Requirement):
    def development(self):
        print("Step 2 Development 2")

class Testing(Development):
    def testing(self):
        self.requirement1()
        self.development()
        print("Step 3 Testing 3")

test_proj = Testing()
test_proj.testing()
