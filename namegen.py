from random import randint
dragname = ["Abraxas",
'Akhekhu',
"Amphiptere",
"Ananta",
"Archion",
"Abeloth",
"Ancestialian",
"Armorwing",
"Anbraxas",
"Ancalagon",
"Apalala",
"Apep",
"Apophis",
"Apsu",
"Brinsop",
"Blaze",
"Bullet",
"Blacksmith",
"Bonescraper",
"Crimson",
"Cyndaquil",
'Cloud',
'Chrysophylax',
'Drachenstein',
'Dart',
'Dratini',
'Drago',
'Drogon',
'Deadheart',
'Deathclaws',
'Eingana',
'Everest',
'Ember',
'Fafnir',
'Froststorm',
'Flurry',
'Falkor',
'Galeru',
'Glaurung',
'Gleep',
'Haku',
'Helios',
'Hyperion'
]

pengname = ['Skipper', 'Rico', 'Kowalski', 'Private']
    


prefix = ("Coder", "Vegan", "Man", "Hacker", "Horse", "Bear", "Goat", "Goblin", "Learner", "Killer", "Woman", "Programmer", "Spy", "Stalker", "Spooderman", "Carrot", "Goat", "Quickscoper", "Quickscoper")

surname = {'january' : "of the Moonlight",
'febuary': 'of the Deep', 'march':'of Ursa Major', 'april': 'of Ursa Minor', 'may': 'of Seville', 'june': 'the Scryer', 'july' : 'the Omniscient', 'august': 'Autumn Nightmare', 'september': 'Wof the Wilds', 'october': 'Blackheart', 'november': 'Summers Fall','december': 'Winters Bane'}



idx= randint(0, len(dragname) - 1)
print(f"{dragname[idx]}")


class Dragon_name:
    


    def __init__(self, name, month):
        self.name = name
        self.month = month
    
    def __str__(self):
        idx= randint(0, len(dragname) - 1)
        self.name = (f"{dragname[idx]}")
        self.month = surname[self.month]
       
    
        return f'{self.name} {self.month}'
# class Penguin_name:
        
class Penguin_name:
    def __init__(self, name, month):
        self.name = name
        self.month = month
    def __str__(self):
        idxp= randint(0, len(prefix) - 1)
        self.name = (f"{prefix[idxp]}")
        idx= randint(0, len(pengname) - 1)
        self.month = (f"{pengname[idx]}")
        return f' TITLE:{self.name} NAME: {self.month}'
        
    




while True:
    peng_or_drag = input('Penguin or Dragon name or press E to exit?').lower()


    if peng_or_drag[0] == 'd':
        

        drag = Dragon_name(input("What is your name"),input('What month were you born').lower())
        print(drag)
        
        
    elif peng_or_drag[0] == 'p':
            peng = Penguin_name(input("What is your name"), input('What month were you born').lower())
            print(peng)
    else:
        break
    
    

    



