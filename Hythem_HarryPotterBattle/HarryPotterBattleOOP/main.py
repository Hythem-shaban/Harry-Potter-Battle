# open the file of the spells
f = open("spells.txt", "r")
contents = f.readlines()
contents[-1] = contents[-1] + '\n'
f.close()
# put the spills in two dictionaries
harrySpells = {}
voldemortSpells = {}
for line in contents:
    line = line.split(" ")
    key = line[1]
    value = line[2]

    if line[0] == 'A':
        harrySpells[key] = int(value)
        voldemortSpells[key] = int(value)

    elif line[0] == 'H':
        harrySpells[key] = int(value)

    elif line[0] == 'V':
        voldemortSpells[key] = int(value)

    else:
        continue
# Creating a class named Wizard
class Wizard:
    def __init__(self):
        self.Health = 100
        self.Energy = 500
        self.countSheild = 3
# Creating a child class called Harry that inherit from Wizard
class Harry(Wizard):
    def __init__(self):
        super().__init__()
        self.Health = 100
        self.Energy = 500
        self.countSheild = 3

# creating an object from class Harry
harry = Harry()

# Creating a child class called Voldemort that inherit from Wizard
class Voldemort(Wizard):
    def __init__(self):
        super().__init__()
        self.Health = 100
        self.Energy = 500
        self.countSheild = 3

# creating an object from class Voldemort
voldemort = Voldemort()

# Creating a child class called Fight that inherit from Harry and Voldemort
class Fight(Harry, Voldemort):
    def __init__(self):
        super().__init__()
    # A method to compare between the energy of the wizard and the power of the spell he says.
    def attack(self, HSpell, VSpell):

        HSpell_Power = harrySpells[HSpell]
        VSpell_Power = voldemortSpells[VSpell]

        if HSpell_Power <= harry.Energy:
            harry.Energy -= HSpell_Power
        else:
            HSpell_Power = 0
        if VSpell_Power <= voldemort.Energy:
            voldemort.Energy -= VSpell_Power
        else:
            VSpell_Power = 0
    # A method to count the number of shields used by each wizard
    # and to determine the damage and the health of each wizard.
    def defend(self, HSpell, VSpell):

        HSpell_Power = harrySpells[HSpell]
        VSpell_Power = voldemortSpells[VSpell]

        if HSpell == "sheild" and VSpell != "sheild":
            if harry.countSheild > 0:
                harry.countSheild -= 1
            else:
                harry.Health -= VSpell_Power

        elif VSpell == "sheild" and HSpell != "sheild":
            if voldemort.countSheild > 0:
                voldemort.countSheild -= 1
            else:
                voldemort.Health -= HSpell_Power

        elif HSpell_Power > VSpell_Power:
            voldemort.Health -= (HSpell_Power - VSpell_Power)

        elif HSpell_Power < VSpell_Power:
            harry.Health -= (VSpell_Power - HSpell_Power)

        else:
            pass
    # A method to display the health and the energy of each wizard after each attack.
    def display_fight(self):
        print("\t\t\tHarry\tVoldmort")
        print("Health : \t", harry.Health, "\t", voldemort.Health)
        print("Energy : \t", harry.Energy, "\t", voldemort.Energy)
    # A method to compare between the health of each wizard after the attack to determine who wins.
    def end_fight(self):
        if voldemort.Health <= 0 and harry.Health > 0:
            return 1
        elif voldemort.Health > 0 and harry.Health <= 0:
            return 2
        elif voldemort.Health <= 0 and harry.Health <= 0:
            return -1
        elif voldemort.Energy <= 0 and harry.Energy <= 0:
            return -2
        else:
            return 0

# creating an object from class Fight
fight = Fight()

# Created an infinite loop using while to take spells from each wizard at each attack.
condition = True
while condition:
    H_Spell, V_Spell = input("Enter the two spells (Harry then voldemort):\n").split()
    fight.attack(H_Spell, V_Spell)
    fight.defend(H_Spell, V_Spell)

    if fight.end_fight() == 0:
        fight.display_fight()
    elif fight.end_fight() == 1:
        fight.display_fight()
        print("\t\tHarry is the winner ..")
        break
    elif fight.end_fight() == 2:
        fight.display_fight()
        print("\t\tVoldemort is the winner ..")
        break
    else:
        print("\t\tNo Energy for both to fight")
        break
