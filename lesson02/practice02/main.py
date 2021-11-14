import random, sys

class LivingCreature:
    health_points = 0
    strength = 0
    vitality = 0

    def decrement_hp(self, value):
        self.health_points -= value

    def is_alive(self):
        if self.health_points > 0:
            return True
        else:
            return False

class Enemy(LivingCreature):
    def __init__(self, strength, vitality):
        self.strength = strength
        self.vitality = vitality
        self.health_points = 1.5 * self.vitality

    def description(self):
        print('***\nEnemy HP:', self.health_points, ' STR:', self.strength, ' VIT:', self.vitality,'\n***\n')

class Spell:
    damage = 0
    name = ''

    def __init__(self, damage, name):
        self.damage = damage
        self.name = name

class Player(LivingCreature):
    name = ''
    level = 1
    magic = 10
    mana_points = 0
    dexterity = 10
    spell = None

    def __init__(self, name):
        self.name = name
        self.vitality = 10
        self.strength = 10
        self.mana_points = 3 * self.magic
        self.health_points = 5 * self.vitality
        self.spell = Spell(2, 'Fireball')

    def description(self):
        print('=====\nName:', self.name, ' level:', self.level)
        print('HP:', self.health_points, ' MP:', self.mana_points)
        print('STR:', self.strength, ' DEX:', self.dexterity, ' VIT:', self.vitality, '\n=====\n')

    def decrement_mp(self, value):
        self.mana_points -= value

    def fight(self, enemy):
        if self.mana_points >= self.spell.damage:
            print('Casting spell:', self.spell.name, 'with damege', self.spell.damage)
            enemy.decrement_hp(self.spell.damage)
            self.decrement_mp(self.spell.damage)
        else:
            self.decrement_hp(enemy.strength)
            enemy.decrement_hp(self.strength)

if __name__ == '__main__':
    print('Please type your character name:')
    name = input()
    player = Player(name)
    player.description()

    while True:
        print('\n************\nNew fight with:')
        enemy = Enemy(random.randint(1, 5), random.randint(1, 5))
        enemy.description()
        while player.is_alive() and enemy.is_alive():
            player.fight(enemy)
        player.description()
        if not player.is_alive():
            break
    print('The end of the end')

