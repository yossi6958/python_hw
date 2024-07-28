from Person import Person


class Student(Person):
    def __init__(self, name='John', age=13):
        super(Student, self).__init__(name, age)
        self.__grade = 0

    def get_grade_avg(self):
        return self.__grade

    def set_grade_avg(self, grade):
        self.__grade = grade
