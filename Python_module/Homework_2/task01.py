class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.skills = ['English']
        self.is_learning = True

    def learn_skill(self, skill_name):
        self.skills.append(skill_name)

    def get_offer(self):
        self.skills_needed = 0
        for i in range(len(self.skills)):
            if self.skills[i] in ['SQL', 'Python', 'Linux', 'English']:
                self.skills_needed += 1
        if self.skills_needed != 4:
            return 'Sorry, you got no offer!'
        else:
            return 'Congrats, you got the offer!'

    def print_result(self):
        print(f'Student name {self.first_name} {self.last_name}, age {self.age}:')
        for i in range(len(self.skills)):
            print(self.skills[i])
        print(f'{self.get_offer()}\n')


john = Student('John', 'Smith', 17)
john.learn_skill('Linux')
john.learn_skill('SQL')
john.learn_skill('Python')

mary = Student('Bloody', 'Mary', 45)
mary.learn_skill('Linux')
mary.learn_skill('SQL')
mary.learn_skill('Python')

peter = Student('Peter', 'Parker', 31)
peter.learn_skill('Linux')
peter.learn_skill('SQL')

john.print_result()
mary.print_result()
peter.print_result()