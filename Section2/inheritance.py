

class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

    @classmethod
    def friend(cls, orgin, friend_name, *args):
        # Returns a new STudent in the same schhol with a new name
        return cls(friend_name, orgin.school, *args)



# print("Tony")
# print("name : {}  School  {}".format(anna.name, anna.school))
# print("name : {}  School  {}".format(kim.name, kim.school))


class WorkingStudent(Student):
    def __init__(self, name, school, salary, jobTitle):
        super().__init__(name, school)
        self.salary = salary
        self.jobTitle = jobTitle

    # @classmethod
    # def friend(cls, friend_name, orgin):
    #     # Returns a new STudent in the same schhol with a new name
    #     return cls(friend_name, orgin, 0)



anna = WorkingStudent("Anna", "Oxford", 20.00,'teacher')
print(anna.salary)


friend = WorkingStudent.friend(anna, "Greg", 17.58, 'Software Decelper')
print(friend.name)
print(friend.school)
print(friend.salary)
print(friend.jobTitle)


# kim = anna.friend("kim","Oxfor")
#
# anna = Student("Anna", "Oxford")
# kim = anna.friend("kim","Oxford")
# tod = WorkingStudent("Tod", "MIT", 40000)
# tony = WorkingStudent.friend('Tony',"MIT")

# # print("Tony")
# print("name : {}  School  {}".format(anna.name, anna.school))
# print("name : {}  School  {}".format(kim.name, kim.school))
# print("name : {}  School  {}   Salary {}  .".format(tod.name, tod.school, tod.salary))
#
# print("name : {}  School  {}   Salary {}  .".format(tony.name, tony.school, tony.salary))


