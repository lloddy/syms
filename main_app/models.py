from django.db import models

# Create your models here.
class Sym:
    def __init__(self, name, gender, age, occupation, description):
        self.name = name
        self.gender = gender
        self.age = age
        self.occupation = occupation
        self.description = description

syms = [
    Sym('Sam', 'Male', '33', 'Astronomer', "He's a bit of a wallflower."),
    Sym('Constance', 'Female', '28', 'Rocket Scientist', "She's just brilliant!"),
    Sym('Mick', 'Male', '52', 'Unemployed', "He's kind of a jerk."),
]