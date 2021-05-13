"""
날짜 : 2021-05-13
이름 : 박재형
내용 : 파이썬 클래스 상속, 다형성 연습문제.
"""


class Person:
    def __init__(self, name):
        self.name = name

        def work(self):
            print("%s working....." % self.name)


class Student(Person):
    def work(self):
        print("%s studying....." % self.name)


class Developer(Person):
    def work(self):
        print("%s programing....." % self.name)


if __name__ == "__main__":

    obj1 = Person("김유신")
    obj2 = Student("김춘추")
    obj3 = Developer("장보고")

    people = [obj1, obj2, obj3]

    for person in people:
        person.work()
