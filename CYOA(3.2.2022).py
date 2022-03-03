### Battle Standard###
def battle(attacker, defender):
  if defender.health<=0:
    attacker.items = attacker.items + " " + defender.items
    attacker.experience = attacker.experience + defender.experience
    # Only apply damage if you need to
    if attacker.attack > defender.defense:
      defender.health = defender.health - (attacker.attack + defender.defense)
    if attacker.playclass== 'Wizard' and defender.playclass== 'Beast':
      print(f"Your {attacker.magic} magic defeats the {defender.name}. You gain {defender.experience} experience.")
    elif attacker.playclass!='Wizard':
         None       
    if defender.attack - attacker.defense > 0:
        print(f"You fight the {defender.name} and take {defender.attack - attacker.defense} damage.")
        attacker.health= attacker.health - (defender.attack - player.defense)

###Standard Question Setup###
def multich(ch1="error1", ch2="error2", ch3="error3", ch4="error4"):
	choice= input(f"""
	Select Option:
		A. {ch1}
		B. {ch2}
		C. {ch3}
		D. {ch4}""")
	return choice
	
###Questions for naming and selecting play class.###
def givename():
	name= input(print("Type your name."))
	return name
def giveclass():
    playclass= multich(ch1='Warrior', ch2='Wizard', ch3='Cleric', ch4='Rogue')
    return playclass
    
#Function to call battler statblock
def playerstatblock():
	self= player
	statblock=print(f"""
	Name: {self.name}
	Location: {self.location}
	Items: {self.items}
	Attack: {self.attack}
	Defense: {self.defense}
	Health: {self.health}
	Magic: {self.magic}
	Experience: {self.experience}
	Level: {self.level}
	Class: {self.playclass}""")
	return self
#playerstatblock()	

#Function to call battler statblock
def enemystatblock():
	self= bandit
	statblock=print(f"""
	Name: {self.name}
	Location: {self.location}
	Items: {self.items}
	Attack: {self.attack}
	Defense: {self.defense}
	Health: {self.health}
	Magic: {self.magic}
	Experience: {self.experience}
	Level: {self.level}
	Class: {self.playclass}""")
	return self
	
	
#Defining the classes for NPC and Battler

class Person:
    def __init__(self, name, location, items):
        self._name = name
        self._location = location
        self._items = items

    @property
    def location(self):
        '''
        Person.attack is a property
        This is the getter method
        '''
        return self._location

    @location.setter
    def location(self, value):
        """
        This is the setter method
        where I can check it's not assigned a value < 0
        """
        if value < 0:
            raise ValueError("Must be >= 0")
        self._location = value

    @property
    def items(self):
        '''
        Person.defense is a property
        This is the getter method
        '''
        return self._items

    @items.setter
    def items(self, value):
        """
        This is the setter method
        where I can check it's not assigned a value < 0
        """
        if value == 0:
            raise ValueError("Must be >= 0")
        self._items = value

    @property
    # Since there is no setter, you can't change the name value.
    def name(self):
        return self._name

    def die(self):
        print(f"{self.name} has died...")
        return


class Battler(Person):
    def __init__(self, name, location, items, health, attack, defense, magic, experience, level, playclass):
        super().__init__(name=name, location=location, items=items)
        self._health= health
        self._attack= attack
        self._defense= defense
        self._magic= magic
        self._experience= experience
        self._level= level
        self._playclass= playclass
 #x       if health <= 0:
#x            raise ValueError()
        
    @property
    def health(self):
        '''
        Person.hp is a property
        This is the getter method
        '''
        return self._health

    @health.setter
    def health(self, value):
        """
        This is the setter method
        where I can check it's not assigned a value < 0
        """
        self._health = value
        if value <= 0:
            self.die()

    @property
    def attack(self):
        return self._attack
        
    @attack.setter
    def attack(self, value):
    	self._attack = value

    @property
    def defense(self):
        return self._defense
        
    @defense.setter
    def defense(self, value):
    	self._defense = value
    	
    @property
    def magic(self):
        return self._magic
        
    @magic.setter
    def magic(self, value):
    	self._magic = value
    	
    @property
    def experience(self):
        return self._experience
        
    @experience.setter
    def experience(self, value):
    	self._experience = value      	
     
    @property
    def level(self):
        return self._level
        
    @level.setter
    def level(self, value):
    	self._level = value
    	
    @property
    def playclass(self):
        return self._playclass
        
    @playclass.setter
    def playclass(self, value):
    	self._playclass = value

    # A method to call when the person finds an item
    def find_item(self, item):
        # Print to users they found something
        self.items= self.items + ' ' + item
        if item[0] in ["a", "e", "i", "o", "u"]:
            print(f"{self.name} found an {item}!")
        else:
            print(f"{self.name} found a {item}!")
        # Add item to inventory list
        self.items = self.items + item
        
###Start PC 'player'.###
player= Battler(name=givename(), location='Town', items=None, health=1, attack=1, defense=1, magic='None', experience=0, level=1, playclass=giveclass())
if player.playclass== 'A':
    player.playclass='Warrior'
    player.items= 'Sword'
    player.attack= 5
    player.defense= 10
    player.health= 15
    player.magic= 'None'
elif player.playclass=='B':
    	player.playclass='Wizard'
    	player.items='Wand'
    	player.attack= 10
    	player.defense= 5
    	player.health= 10
    	player.magic= 'Fire'
elif player.playclass=='C':
    	player.playclass='Cleric'
    	player.items='Relic'
    	player.attack= 4
    	player.defense= 10
    	player.health= 12
    	player.magic= 'Heal'
elif player.playclass=='D':
    	player.playclass='Rogue'
    	player.items='Dagger' +' ' + 'Lockpick'
    	player.attack= 8
    	player.defense= 8
    	player.health= 10
    	player.magic= 'None'
else:
    	raise ValueError('option not supported')
    	
###Start enemies###
#minotaur
minotaur= Battler(name='Minotaur', location='Dungeon', items='Health-Potion', health=20, attack=12, defense=10, magic='None', experience=5, level=1, playclass='Beast')
#zombie
zombie= Battler(name='Zombie', location='Dungeon', items='Poison-Vile', health=10, attack=5, defense=5, magic='Necro', experience=5, level=1, playclass='Undead')
#red drake
red_drakeplayer=Battler(name='Red Drake', location='Dungeon', items='Fire-Flagon', health=5, attack=15, defense=10, magic='Fire', experience=5, level=1, playclass='Dragon')
#Bandit
bandit= Battler(name='Bandit', location='Dungeon', items='Coin', health=1, attack=12, defense=3, magic='None', experience=5, level=1, playclass='Human')

    	
playerstatblock()
enemystatblock()

def fight():
	fight=multich(ch1='Fight', ch2='Run')

fight()
if fight=='A' or 'a':
	battle(attacker = player,  defender = bandit)
	
playerstatblock()