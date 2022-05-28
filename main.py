class Student:
    
    def __init__(self, name, age, tracks, score):
        
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score

    def details(self):
        print('My name is', self.name)
        print('I am', self.age, 'years old.')
        print('My tracks are', self.tracks)
        print('My score is', self.score)

    def change_name(self, name):
        self.name = name

    def change_age(self, age):
        self.age = age

    def add_track(self, tracks):
        self.tracks.append(tracks)
        return self.tracks

    def get_score(self):
        return self.score



Bob = Student("Bob", 26, ["FE","BE"], 20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
Bob.details()
