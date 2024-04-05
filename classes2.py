import classes
from classes import Pokemon as Pokemon
from classes import Player as Player
from classes import osszespokemon as osszespokemon
from classes import load_from_file as load_from_file
import menu
class Player_pokemon:
    def __init__(self, nickname, pokemon: Pokemon, health: int, energy: int) -> None:
        # energy MAX 100pp
        
        self.nickname = nickname
        self.pokemon = pokemon
        self.health = health 
        self.energy = energy
    
    def damage(self, damage: int):
        self.health -= damage
        return f"{self.nickname} took {damage}hp damage, health is now {self.health}hp"
    
    def damage_percent(self, damage_percent: int):
        damaged_hp = round(self.pokemon.health * damage_percent / 100)
        self.health -= damaged_hp
        return f"{self.nickname} took {damaged_hp}hp damage, health is now {self.health}hp"
    
    def use_energy(self, used_energy: int):
        self.energy -= used_energy
        return f"{self.nickname} used {used_energy}pp, energy level is now {self.energy}pp"
    
    def heal_percent(self, healing_percent: int):
        healed_hp = round(self.pokemon.health * healing_percent / 100)
        self.health += healed_hp
        if self.health > self.pokemon.health:
            self.health = self.pokemon.health
            return f"{self.nickname} healed fully"
        else:
            return f"{self.nickname} healed {healed_hp}hp and now has {self.health}hp"
    
    def heal_hp(self, healing_hp: int):
        self.health += healing_hp
        if self.health > self.pokemon.health:
            self.health = self.pokemon.health
            return f"{self.nickname} healed fully"
        else:
            return f"{self.nickname} healed {healing_hp}hp and now has {self.health}hp"
    
    def pick_item(self, player: Player, num_of_first = 0):
        classes.clearscreen()
        if num_of_first <0: num_of_first = 0
        choice = menu.generic_menu("Összes itemed", ["Vissza","Fel", player.items[num_of_first + 0].name, player.items[num_of_first + 1].name, player.items[num_of_first + 2].name, player.items[num_of_first + 3].name, player.items[num_of_first + 4].name, player.items[num_of_first + 5].name, player.items[num_of_first + 6].name, "Tovább"])
        match choice:
            case "1":
                return True
            case "2":
                back = self.pick_item(player, num_of_first - 5)
                if back == True:
                    return True
            case "10":
                back = self.pick_item(player, num_of_first + 5)
                if back == True:
                    return True
            case _:
                if choice.isnumeric():
                    if int(choice) in [3,4,5,6,7,8,9]:
                        self.use_item(num_of_first + (int(choice)-3), player)
    def use_item(self, item_num: int, player: Player):
        if self.health <= 0:
            return "Halott pokemon nem használhat itemet!"
        item = player.items[item_num]
        self.health += item.heal
        self.health = min(self.health, self.pokemon.health)
        self.pokemon.speed += item.speed
        self.pokemon.defe += item.defe
        self.pokemon.atk += item.atk
        
        player.items.pop(item_num)
        
        return item.desc

class Item:
    def __init__(self, row) -> None:
        self.num = row[0]
        self.name = row[1]
        self.desc = row[2]
        self.defe = row[3]
        self.atk = row[4]
        self.speed = row[5]
        self.heal = row[6]

all_items: list[Item] = []
load_from_file('items.csv', Item, all_items)
        


    