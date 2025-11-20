# Single Inheritance

class Flowers:
    rose = "Rose Flower"
    lotus = "Lotus Flower"
    marrigold= "Marrigold Flower"

    def __init__(self, type1, type2):
        self.type = type1
        self.type = type2
        print("Different flowers: ",self.rose, self.lotus, self.marrigold)

    def m_rose(self):
        self.rose = "Red"
        print("My rose is", self.rose)

class Flowers2(Flowers):

    def m_chinese_rose(self):
        self.rose = "Chinese Rose"
        print("My chinese rose is", self.rose)

flower1 = Flowers2("Red", "Chinese Rose")
flower1.m_chinese_rose()
flower1.m_rose()


