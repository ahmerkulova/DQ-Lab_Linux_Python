class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.skills = ['English']
        self.results = ['Passed']
        self.is_learning = True

    def got_skill(self, skill_name, result):
        self.skills.append(skill_name)
        self.results.append(result)

    def got_offer(self):
        self.counter = 0
        for i in range(len(self.results)):
            if self.results[i] in 'Passed':
                self.counter += 1
        if self.counter == 4:
            return f'{self.counter} of {len(self.results)} - congrats, you got the offer!'
        else:
            return f'{self.counter} of {len(self.results)} - sorry, you got no offer!'

    def result_info(self):
        print(f'Student name {self.first_name} {self.last_name}, age {self.age}:')
        for i in range(len(self.skills)):
            print(f'\t{self.skills[i]} result: {self.results[i]}')
        print(f'{self.got_offer()}\n')

john = Student('John', 'Smith', 17)
john.got_skill('Linux', 'Passed')
john.got_skill('SQL', 'Passed')
john.got_skill('Python', 'Passed')

mary = Student('Bloody', 'Mary', 45)
mary.got_skill('Linux', 'Passed')
mary.got_skill('SQL', 'Failed')
mary.got_skill('Python', 'Failed')

peter = Student('Peter', 'Parker', 31)
peter.got_skill('Linux', 'Passed')
peter.got_skill('SQL', 'Passed')
peter.got_skill('Python', 'Passed')

john.result_info()
mary.result_info()
peter.result_info()