print("Lesson-4")

class Human:
    def __init__(self, name):
        self.Name = name

class Auto:
    def __init__(self, brand):
        self.Brand = brand
        self.Humans = []
    def AddHuman(self, Human):
        self.Humans.append(Human)
    def PrintHumans(self):
        if self.Humans != []:
            print("Human Names:")
            for Human in self.Humans:
                print("\t",Human.Name)
        else:
            print("This auto is empty")

human1 = Human("Victo Pavlik")
human2 = Human("Yarosh Bohdan")

autoBohdan = Auto("Bohdan")

print("Auto-Brend:", autoBohdan.Brand)

autoBohdan.AddHuman(human1)
autoBohdan.AddHuman(human2)

autoBohdan.AddHuman(Human("Tymofii Moisei"))

autoBohdan.PrintHumans()