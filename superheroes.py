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
        

    def attack(self):
        ''' Return a value between 0 and the value set by self.max_damage.'''

        # Pick a random value between 0 and self.max_damage
        attack_value = random.randint(0,self.max_damage)
        return attack_value
    
class Weapon(Ability):
    def attack(self):
        """  This method returns a random value
        between one half to the full attack power of the weapon.
        """
        # TODO: Use integer division to find half of the max_damage value
        # then return a random integer between half of max_damage and max_damage
        
        weapon_attack_value = random.randint(self.max_damage//2, self.max_damage)
        return weapon_attack_value

# Armour Class
class Armour:
    def __init__(self, name, max_block):
        '''Instantiate instance properties.
            name: String
            max_block: Integer
        '''
        self.name = name
        self.max_block = max_block
        

    def block(self):
        '''
        Return a random value between 0 and the
        initialized max_block strength.
        '''
        random_value = random.randint(0, self.max_block)
        print(f"Your {self.name} blocked {random_value} damage!")
        return random_value

# Hero Class
class Hero:
    def __init__(self, name, starting_health=100, deaths=0, kills=0):
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
        print("Ability Engaged")
        
    def add_weapon(self, weapon):
        '''Add weapon to self.abilities'''
        # TODO: This method will append the weapon object passed in as an
        # argument to self.abilities.
        # This means that self.abilities will be a list of
        # abilities and weapons.
        self.abilities.append(weapon)
        print("Weapon Equipped")
        
    def add_armour(self, armour):
        '''Add armour to self.armours
            Armour: Armour Object
        '''
        self.armours.append(armour)
        print("Armour Equipped")
        
    def add_kill(self, num_kills):
        self.kills += num_kills
    
    def add_death(self, num_deaths):
        self.deaths += num_deaths

        
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
        
    
    def defend(self):
        '''Calculate the total block amount from all armor blocks.
        return: total_block:Int
        '''
        total_block = 0
        # incoming_damage = 0
        for block in self.armours:
            total_block += block.block()
            print(f"Total Block: {total_block}")
        return int(total_block)
    
    
    def take_damage(self, damage):
        '''Updates self.current_health to reflect the damage 
        minus the defense.
        '''
        defense = self.defend()    
        self.current_health -= damage - defense
        print(f"{self.name}'s current health is {self.current_health}")
    
    def is_alive(self):
        '''Return True or False depending on whether 
        the hero is alive or not.
        '''
        if self.current_health <= 0:
            print(f"{self.name} sustained too much damage and has died!")
            return False
        else:
            return True
    
    
    def fight(self, opponent):
        ''' Current Hero will take turns fighting the opponent hero passed in.
        '''
        print(f"A fight has broken out between {self.name} and {opponent.name}! There can only be one victor. Who will it be?")
        while self.is_alive() and opponent.is_alive():
            if self.abilities or opponent.abilities:
                self.take_damage(opponent.attack())
                opponent.take_damage(self.attack())
                print("Round One: Fight!")
            else:
                print("Draw")
                
        if self.is_alive() == False and opponent.is_alive() == True:
            print(f"{opponent.name} is the victor! They will dance on {self.name}'s grave as soon as it has been dug.")
            opponent.add_kill(1)
            self.add_death(1)
        elif self.is_alive() == True and opponent.is_alive() == False:
            print(f"{self.name} is the victor! They will celebrate this win when the battle is over.")
            self.add_kill(1)
            opponent.add_death(1)
        elif self.is_alive() == False and opponent.is_alive() == False:
            print(f"{self.name} and {opponent.name} both died. There is no victor this time, only pain and regret!")
            opponent.add_kill(1)
            self.add_death(1)
            self.add_kill(1)
            opponent.add_death(1)
            
class Team:
    def __init__(self, name):
        ''' Initialize your team with its team name and an empty list of heroes
        '''
        self.name = name
        self.heroes = list()
        self.num_kills = 0
        
    def add_hero(self, hero):
        self.heroes.append(hero)
    
    def remove_hero(self, name):
        '''Remove hero from heroes list.
        If Hero isn't found return 0.
        '''
        foundHero = False
        if len(self.heroes) <=0:
            return 0
        # loop through each hero in our list
        for hero in self.heroes:
            # if we find them, remove them from the list
            if hero.name == name:
                self.heroes.remove(hero)
                # set our indicator to True
                foundHero = True
            if not foundHero:
                return 0
        
    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)
            
    def team_attack(self, opponents):
        """Randomly select a living hero from each team and 
        have them fight until one or both teams have no surviving heroes."""
        
        living_heroes = list()
        dead_heroes = list()
        living_opponents = list()
        dead_opponents = list()
        
        for hero in self.heroes:
            if hero.is_alive():
                living_heroes.append(hero)
            
        for hero in opponents.heroes:
            if hero.is_alive():
                living_opponents.append(hero)
            
        while len(living_heroes) > 0 and len(living_opponents) > 0:
            random_hero = random.choice(self.heroes)
            random_opponent = random.choice(opponents.heroes)
            if random_hero.is_alive() and random_opponent.is_alive():
                random_hero.fight(random_opponent)
            while hero in living_heroes:
                if random_hero.is_alive() == False and random_opponent.is_alive() == True:
                    dead_opponents.append(random_opponent)
            while hero in living_opponents:
                if random_hero.is_alive() == True and random_opponent.is_alive() == False:
                    dead_heroes.append(random_hero)
            break
            
        
    def revive_heroes():
        for hero in self.heroes:
            hero.current_health = hero.starting_health
        
        
    def stats():
        """Print team statistics"""
        print(self.name)
        for hero in self.heroes:
            kd = hero.kills / hero.deaths
            print("{} Kill/Deaths:{}".format(hero.name,kd))
        
        
        

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    # ability = Ability("Debugging Ability", 20)
    # another_ability = Ability("Smarty Pants", 90)
    # print(ability.name)
    # print(ability.attack())
    # armour = Armour("Debugging Shield", 10)
    # print(armour.name)
    # print(armour.block())
    # my_hero = Hero("Grace Hopper", 200)
    # print(my_hero.name)
    # print(my_hero.current_health)
    # my_hero.add_ability(ability)
    # my_hero.add_ability(another_ability)
    # print(my_hero.abilities)
    # print(my_hero.attack())
    
    # hero = Hero("Grace Hopper", 200)
    # hero.take_damage(150)
    # print(hero.is_alive())
    # hero.take_damage(15000)
    # print(hero.is_alive())
    # print(f"{hero.name}'s current health is {hero.current_health}")
    
    # hero1 = Hero("Wonder Woman")
    # hero2 = Hero("Dumbledore")
    # ability1 = Ability("Super Speed", 300)
    # ability2 = Ability("Super Eyes", 130)
    # ability3 = Ability("Wizard Wand", 80)
    # ability4 = Ability("Wizard Beard", 20)
    # hero1.add_ability(ability1)
    # hero1.add_ability(ability2)
    # hero2.add_ability(ability3)
    # hero2.add_ability(ability4)
    # hero1.fight(hero2)
    
    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())