import random

def validator(list_of_valid_entries, input_text):
    is_valid = False
    while True:
        try:
            entry = input(input_text)
            for item in list_of_valid_entries:
                if item == entry:
                    is_valid = True
                else:
                    pass
            if is_valid:
                return entry
            else:
                print("Invalid Input! Try again...")
        except:
            print("Invalid Input! Try again...")

def validator_num(input_text):
    is_valid = False
    while True:
        try:
            entry = input(input_text)
            if entry.isdigit()== True:
                is_valid = True
                return entry
            else:
                print("Invalid Input! Try again...")
        except:
            print("Invalid Input! Try again...")

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
            armours: List
            name: String
            starting_health: Integer
            current_health: Integer
        '''
        
        self.abilities = list()
        self.armours = list()
        self.weapons = list()
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
        self.weapons.append(weapon)
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
            print(ability)
            # add the damage of each attack to our running total
            total_damage += ability.attack()
            print(f"Total Damage: {total_damage}")
        return int(total_damage)
        
    
    def defend(self):
        '''Calculate the total block amount from all armour blocks.
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
        if defense >= damage:
            self.current_health -= 0
        else:
            self.current_health -= (damage - defense)
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
            
    def attack(self, opponents):
        """Randomly select a living hero from each team and 
        have them fight until one or both teams have no surviving heroes."""
        
        living_heroes = list()
        dead_heroes = list()
        living_opponents = list()
        dead_opponents = list()
        
        for hero in self.heroes:
            if hero.is_alive():
                living_heroes.append(hero)
            else:
                dead_heroes.append(hero)
            
        for hero in opponents.heroes:
            if hero.is_alive():
                living_opponents.append(hero)
            else:
                dead_opponents.append(hero)
            
        while len(living_heroes) > 0 and len(living_opponents) > 0:
            # As long as there are living heroes on both sides...
            random_hero = random.choice(self.heroes)
            random_opponent = random.choice(opponents.heroes)
            # Pick one from each side...
            if random_hero.is_alive() and random_opponent.is_alive():
                # And have them fight
                random_hero.fight(random_opponent)
                # When one of them dies, remove them from the list of living heroes, and add them to the list of dead heroes
                if random_hero.is_alive() == False and random_opponent.is_alive() == True:
                    dead_heroes.append(random_hero)
                    living_heroes.remove(random_hero)
                elif random_hero.is_alive() == True and random_opponent.is_alive() == False:
                    dead_opponents.append(random_opponent)
                    living_opponents.remove(random_opponent)
            # break
            
        
    def revive_heroes(self):
        for hero in self.heroes:
            hero.current_health = hero.starting_health
        
        
    def stats():
        """Print team statistics"""
        print(self.name)
        for hero in self.heroes:
            kd = hero.kills / hero.deaths
            print("{} Kill/Deaths:{}".format(hero.name,kd))
        
        
class Arena:
    def __init__(self):
        '''Instantiate properties
            team_one: None
            team_two: None
        '''
        self.team_one = None
        self.team_two = None
        
    def create_ability(self):
        '''Prompt for Ability information.
        return Ability with values from user Input
        '''
        name = input("What is the ability name?  ")
        max_damage = input(
            "What is the max damage of the ability?  ")
        return Ability(name, max_damage)
    
    def create_weapon(self):
        '''Prompt user for Weapon information
        return Weapon with values from user input.
        '''
        name = input("What is the weapon name?  ")
        max_damage = input(
            "What is the max damage of the weapon?  ")
        return Weapon(name, max_damage)
    
    def create_armour(self):
        '''Prompt user for armour information
        return armour with values from user input.
        '''
        name = input("What is the armour name?  ")
        max_block = input(
            "What is the max block of the armour?  ")
        return Armour(name, max_block)
    
    def build_abilities_list(self):
        # Return an ability and append ability
        abilities = [
            "Spinning Bird Kick",
            "Flashbang",
            "Dazzle",
            "Invulnerability",
            "BAMF!",
            "Telekenesis",
            "Rain of Frogs",
            "Pym Particles",
            "Super Stretchy",
            "Lava Hands",
            "Multiplicity",
            "One Inch Punch",
            "Assumed Superiority",
            "Hella Henchmen"]
        # Get one abilitiy out of the list
        index = random.randint(0, len(abilities) - 1)
        ability_name = abilities[index]
        abil_att_Strength = random.randint(0, 500)
        one_ability = Ability(ability_name, abil_att_Strength)
        return one_ability
        # hero.add_ability(one_ability) # <-- Doing this in create_hero
        
    def build_weapons_list(self):
        # Return a weapon and append to weapons list
        weapons = [
            "Adamantium Claws",
            "Staff of Oblivion",
            "Strobe Light",
            "Grapefruit Spoon",
            "Pocketful of Angry Weasels",
            "Nancy Pelosi",
            "Acupuncture Needles",
            "Kinetically Charged Playing Cards",
            "Ball and Chain",
            "Morningstar",
            "Nunchucks",
            "Surface to Air Missiles",
            "Bowel Disruptor Ray Gun",
            "Infuse Bystanders with Envy"]
        # Get one weapon out of the list
        index = random.randint(0, len(weapons) - 1)
        weapon_name = weapons[index]
        abil_att_Strength = random.randint(0, 500)
        one_weapon = Weapon(weapon_name, abil_att_Strength)
        return one_weapon
        # hero.add_weapon(one_weapon) # <-- Doing this in create_hero

    def build_armours_list(self):
        armours = [
            "Chain Mail",
            "Forcefield",
            "Energy Absorption",
            "Woad",
            "Riot Gear",
            "Sun Hat",
            "Turtle Shell",
            "Kevlar Suit",
            "Invisibility",
            "Skunk Power",
            "Battle Suit",
            "Jockstrap",
            "Ion Shield",
            "Shroud of Mystery"]
        # Get one armour out of the list
        index = random.randint(0, len(armours) - 1)
        armour_name = armours[index]
        defense = random.randint(0, 500)
        one_armour = Armour(armour_name, defense)
        return one_armour
    
    def create_hero(self):
        '''Prompt user for Hero information
        return Hero with values from user input.
        '''
        heroes = [
            "Captain Planet",
            "Colin Kaepernick",
            "Optimus Prime",
            "Harriet Tubman",
            "Frankenstein",
            "Animal Man",
            "Johnny Alpha",
            "Durham Red",
            "Nikolai Dante",
            "Banana Man",
            "Black Widow",
            "Cable",
            "Deadpool",
            "Namor",
            "Wolverine",
            "Jubilee",
            "Elektra",
            "Hulk",
            "Moon Knight",
            "Future Man",
            "Avatar Korra",
            "Desperate Dan",
            "Nightcrawler"]
        index = random.randint(0, len(heroes) - 1)
        hero_name = heroes[index]
        hero = Hero(hero_name)
        # Ask how many abilities does the hero have then build that many abilities
        abilites_number = int(validator_num("How many abilities do you want your hero {} to have? ".format(hero.name)))
        for _ in range(0, abilites_number):
            ability = self.build_abilities_list()
            hero.add_ability(ability)
            print(ability.name)
        weapons_number = int(validator_num("How many weapons do you want your hero {} to have? ".format(hero.name)))
        for _ in range(0, weapons_number):
            weapon = self.build_weapons_list()
            hero.add_weapon(weapon)
            print(weapon.name)
        # Ask How many armour
        armours_number = int(validator_num("How many pieces of armour do you want your hero {} to have? ".format(hero.name)))
        # However many armour the user wants the hero get the ability and add to the heros list of armour that many times
        for _ in range(0, armours_number):
            armour = self.build_armours_list()
            hero.add_armour(armour)
            print(armour.name)
        return hero
    
    def build_team_one(self):
        '''Prompt the user to build team_one '''
        print("This is the Superhero Dueler! Welcome to the Pit of Despair:\n")
        print("   Two teams enter, and only one team leaves.\n")

        # TODO: This method should allow a user to create team one.
        # 1) Prompt the user for the name of the team
        team_one_name = input("Team One's name: ")
        # 2) Prompt the user for the number of Heroes on the team
        team_size = int(input(f"How many heroes are on {team_one_name}? Please enter an integer.\n"))
        # 3) Instantiate a new Team object,
        # using the team name obtained from user input
        self.team_one = Team(team_one_name)
        # 4) use a loop to call self.create_hero() for the number
        # of heroes the user specified the team should have,
        # and then add the heroes to the team.
        for _ in range(0, team_size):
            self.team_one.heroes.append(self.create_hero())
        
    
    def build_team_two(self):
        '''Prompt the user to build team_two'''
        # TODO: This method should allow a user to create team two.
        # 1) Prompt the user for the name of the team
        team_two_name = input("Team Two's name: ")
        # 2) Prompt the user for the number of Heroes on the team
        team_size = int(input(f"How many heroes are on {team_two_name}? Please enter an integer.\n"))
        # 3) Instantiate a new Team object,
        # using the team name obtained from user input
        self.team_two = Team(team_two_name)
        # 4) use a loop to call self.create_hero() for the number
        # of heroes the user specified the team should have,
        # and then add the heroes to the team.
        for _ in range(0, team_size):
            self.team_two.heroes.append(self.create_hero())
        
    def team_battle(self):
        '''Battle team_one and team_two together.'''
        # TODO: This method should battle the teams together.
        # Call the attack method that exists in your team objects
        # for that battle functionality.
        self.team_one.attack(self.team_two)
        
    def show_stats(self):
        '''Prints team statistics to terminal.'''
        # TODO: This method should print out battle statistics
        # including each team's average kill/death ratio.
        team_one_kills = 0
        team_one_deaths = 0
        team_two_kills = 0 
        team_two_deaths = 0
        kd1 = 0
        kd2 = 0
        
        # if team_one_deaths == 0:
        #     kd1 = team_one_kills
        # elif team_two_deaths == 0:
        #     kd2 = team_two_kills
        # else:
        #     kd1 = team_one_kills / team_one_deaths
        #     kd2 = team_two_kills / team_two_deaths
        print("{} Kill/Deaths:{}".format(self.team_one.name, kd1))
        print("{} Kill/Deaths:{}".format(self.team_two.name, kd2))
        if team_one_deaths == len(self.team_one.heroes) and team_two_deaths < len(self.team_two.heroes):
            print(f"{self.team_two} wins!")
        elif team_two_deaths == len (self.team_two.heroes)and team_one_deaths < len(self.team_one.heroes):
            print(f"{self.team_one} wins!")
        else:
            print("It's a draw!")
                
        for hero in self.team_one.heroes:
            team_one_kills += hero.kills
            team_one_deaths +=  hero.deaths
        for hero in self.team_two.heroes:
            team_two_kills += hero.kills
            team_two_deaths += hero.deaths
        try:
            team_1_kd = team_one_kills / team_one_deaths
        except ZeroDivisionError:
            team_1_kd = team_one_kills
        try:
            team_2_kd = team_two_kills / team_two_deaths
        except ZeroDivisionError:
            team_2_kd = team_two_kills
        
        print("Team 1's KD is: {}".format(str(team_1_kd)))
        print("Team 2's KD is: {}".format(str(team_2_kd)))
            
        for hero in self.team_one.heroes:
            if hero.is_alive():
                print(f"{hero.name} from {self.team_one.name} survived!")
                
        for hero in self.team_two.heroes:
            if hero.is_alive():
                print(f"{hero.name} from {self.team_two.name} survived!")
                
        # Required Stats:
        #     Show surviving heroes.
        #     Declare winning team
        #     Show both teams average kill/death ratio.
        # Some help on how to achieve these tasks:
        # TODO: for each team, loop through all of their heroes,
        # and use the is_alive() method to check for alive heroes,
        # printing their names and increasing the count if they're alive.
        #
        # TODO: based off of your count of alive heroes,
        # you can see which team has more alive heroes, and therefore,
        # declare which team is the winning team
        #
        # TODO for each team, calculate the total kills and deaths for each hero,
        # find the average kills and deaths by dividing the totals by the number of heroes.
        # finally, divide the average number of kills by the average number of deaths for each team
        pass

if __name__ == "__main__":
    game_is_running = True
    arena = Arena()
    arena.build_team_one()
    arena.build_team_two()
    arena.team_battle()
    arena.show_stats()
    
    # while condition is true run this code
    while game_is_running:
        # teams battle
        arena.team_battle()
        # show kill/death ratio of each hero
        arena.show_stats()
        # After game ask user do they want to play again
        play_again = validator(["Yes","yes","y", "Y", "No", "no", "n", "N"],"Play Again? Y or N: ")
        if play_again ==  "No" or play_again ==  "no" or play_again ==  "n" or play_again == "N":
            game_is_running = False

        else:
            recreate_teams = validator(["Yes","yes","y", "Y", "No", "no", "n", "N"],"Do you want new teams? (Y/N)")
            if recreate_teams == "y" or "Y" or "Yes" or "yes":
                arena.build_team_one()
                arena.build_team_two()
            else:
                # Revive heroes to play again
                # call function that resets all heroes to original value health
                arena.team_one.revive_heroes()
                arena.team_two.revive_heroes()
    
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
    
    # hero = Hero("Wonder Woman")
    # weapon = Weapon("Lasso of Truth", 90)
    # hero.add_weapon(weapon)
    # print(hero.attack())