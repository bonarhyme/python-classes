class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score ):
        if (isinstance(name, str)):
            self.name = name
        else:
            print("Name must be a string.")
            return

        if (isinstance(age, int)):
            self.age = age
        else:
            print("Age must be a whole number.")
            return

        if (isinstance(tracks, list)):
            self.tracks = tracks
        else:
            print("Tracks must be a list.")
            return

        if (isinstance(score, float)):
            self.score = score
        else:
            print("Score must be a float.")
            return

    def change_name(self, name):
        if (isinstance(name, str)):
            self.name = name
        else:
            print("You must povide a string.")
            raise TypeError("Only strings are allowed")


    def change_age(self, age):
        if (isinstance(age, int)):
            self.age = age
        else:
            print("You must povide a number.")
            raise TypeError("Only integers are allowed")

    def add_track(self, track):
        self.tracks.append(track)

    def  get_score(self):
        return self.score

Bob = Student(name="Sunday", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(7)
Bob.add_track("UI/UX")
score = Bob.get_score()
print(score)
