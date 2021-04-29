# (1) 클래스 정의

class Computer:
    # 속성
    def __init__(self, brand, cpu, ram, hdd):
        self.brand = brand
        self.cpu = cpu
        self.ram = ram
        self.hdd = hdd

    # 기능
    def calc(self):
        print("Computer calc...")

    def info(self):
        print("-----------------")
        print("제조사", self.brand)
        print("cpu 사양: ", self.cpu)
        print("ram 사양: ", self.ram)
        print("hdd 사양: ", self.hdd)
