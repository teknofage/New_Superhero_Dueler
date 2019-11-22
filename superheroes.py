import random

# Ability Class
class Ability:
    def __init__(self, name, max_damage):
        '''Initialize the values passed into this method 
        as instance variables.
            '''

        # Assign the "name" and "max_damage"
        # for a specific instance of the Ability class
        self.name = name
        self.max_damage = max_damage
        print("Ability Created")

    def attack(self):
        ''' Return a value between 0 and the value set by self.max_damage.'''

        # Pick a random value between 0 and self.max_damage
        attack_value = random.randint(0,self.max_damage)
        return attack_value

# Armour Class
class Armour:
    def __init__(self, name, max_block):
        '''Instantiate instance properties.
            name: String
            max_block: Integer
        '''
        self.name = name
        self.max_block = max_block
        print("Armour Created")

    def block(self):
        '''
        Return a random value between 0 and the
        initialized max_block strength.
        '''
        block_value = random.randint(0,self.max_block)
        return block_value

# Hero Class
class Hero:
    def __init__(self, name, starting_health=100):
        '''Instance properties:
            abilities: List
            armors: List
            name: String
            starting_health: Integer
            current_health: Integer
        '''
        
        self.abilities = list()
        self.armours = list()
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.deaths = 0
        self.kills = 0
        
        
    def add_ability(self, ability):
        ''' Add ability to abilities list '''
        self.abilities.append(ability)
        
    def add_armour(self, armour):
        '''Add armour to self.armors
            Armour: Armour Object
        '''
        self.armours.append(armour)

        
    def attack(self):
        # start our total out at 0
        '''Calculate the total damage from all ability attacks.
            return: total_damage:Int
        '''        
        total_damage = 0
        # loop through all of our hero's abilities
        for ability in self.abilities:
            # add the damage of each attack to our running total
            total_damage += ability.attack()
            print(f"Total Damage: {total_damage}")
        return int(total_damage)
        
    
    def defend(self, incoming_damage):
        '''Calculate the total block amount from all armor blocks.
        return: total_block:Int
        '''
        total_block = 0
        for armour in self.armours:
            total_block += armour.block_value
            print(f"Total Block: {total_block}")
        return int(total_block)
    
    
    # def take_damage(damage):
    #     pass
    # def is_alive():
    #     pass
    # def fight():
    #     pass

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    ability = Ability("Debugging Ability", 20)
    another_ability = Ability("Smarty Pants", 90)
    print(ability.name)
    print(ability.attack())
    armour = Armour("Debugging Shield", 10)
    print(armour.name)
    print(armour.block())
    my_hero = Hero("Grace Hopper", 200)
    print(my_hero.name)
    print(my_hero.current_health)
    my_hero.add_ability(ability)
    my_hero.add_ability(another_ability)
    print(my_hero.abilities)
    print(my_hero.attack())