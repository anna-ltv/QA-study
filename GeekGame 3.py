player_name = input('Enter name:')
player = {'name': player_name, 'health': 100, 'damage': 50, 'armor': 1.2}

enemy_name = input('Enter name:')
enemy = {'name': enemy_name, 'health': 100, 'damage': 30, 'armor': 1}

def get_damage(damage, armor):
    return damage/armor

def attack(attacker, attacked):
    damage = get_damage(attacker['damage'], attacked['armor'])
    attacked['health'] -= damage

attack(enemy, player)
print(enemy)
print(player)
print('-'*50)

attack(player, enemy)
print(player)
print(enemy)