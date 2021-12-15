class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.skills = ['English']
        self.skills_needed = ['English', 'SQL', 'Python', 'Linux']
        self.enroll_training()

    def __str__(self):
        return f'Student name {self.first_name} {self.last_name}, age {self.age}:'

    def enroll_training(self):
        self.is_learning = True

    def learn_skill(self, skill_name):
        self.skills.append(skill_name)

    def make_offer(self):
        for item in self.skills_needed:
            if item not in self.skills:
                return False
            else:
                continue
        return True


john = Student('John', 'Smith', 17)
john.learn_skill('Linux')
john.learn_skill('SQL')
john.learn_skill('Python')
john.learn_skill('C++')

mary = Student('Bloody', 'Mary', 45)
mary.learn_skill('Linux')
mary.learn_skill('SQL')
mary.learn_skill('Python')

peter = Student('Peter', 'Parker', 31)
peter.learn_skill('Linux')
peter.learn_skill('SQL')

print(john.__str__())
print(f'\tGot offer: {john.make_offer()}')
print(mary.__str__())
print(f'\tGot offer: {mary.make_offer()}')
print(peter.__str__())
print(f'\tGot offer: {peter.make_offer()}')