class Personnage:
    TYPE="AI"
    def __init__(self, name="Americ"):
        self.name = name
        self.poste = "None"
        print("Iniialisation de la classe:name=" + self.name)
    def greeting(self):
        print("Bonjour je suis " + self.name)
        print("         je suis " + self.poste)
