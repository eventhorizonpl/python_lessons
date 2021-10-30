import random, sys

class Enemy:
    health_points = 0
    strength = 0
    vitality = 0

    def __init__(self, strength, vitality):
        self.strength = strength
        self.vitality = vitality
        self.health_points = 1.5 * self.vitality

    def description(self):
        print('HP:', self.health_points, ' STR:', self.strength, ' VIT:', self.vitality)

    def decrement_hp(self, value):
        self.health_points -= value

    def get_strength(self):
        return self.strength

    def is_alive(self):
        if self.health_points > 0:
            return True
        else:
            return False

class Player:
    name = ''
    level = 1
    health_points = 0
    mana_points = 0
    strength = 10
    dexterity = 10
    vitality = 10

    def __init__(self, name):
        self.name = name
        self.health_points = 5 * self.vitality

    def description(self):
        print('Name:', self.name, ' level:', self.level)
        print('HP:', self.health_points, ' MP:', self.mana_points)
        print('STR:', self.strength, ' DEX:', self.dexterity, ' VIT:', self.vitality)

    def fight(self, enemy):
        self.decrement_hp(enemy.get_strength())
        enemy.decrement_hp(self.strength)

    def decrement_hp(self, value):
        self.health_points -= value

    def get_strength(self):
        return self.strength

    def is_alive(self):
        if self.health_points > 0:
            return True
        else:
            return False

if __name__ == '__main__':
    print('Please type your character name:')
    name = input()
    player = Player(name)
    player.description()
    #print('Is he alive', player.is_alive())
    #sys.exit()

    while True:
        print('\n************\nNew fight with:')
        enemy = Enemy(random.randint(1, 5), random.randint(1, 5))
        enemy.description()
        while player.is_alive() and enemy.is_alive():
            player.fight(enemy)
        player.description()
        if not player.is_alive():
            break
        #print('Is he alive', enemy.is_alive())
    print('The end of the end')

