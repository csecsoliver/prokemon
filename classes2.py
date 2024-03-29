import classes
class Player_pokemon:
    def __init__(self, nickname, pokemon: classes.Pokemon, health: int, energy: int) -> None:
        # [name, nickname]
        
        self.nickname = nickname
        self.pokemon = pokemon
        self.health = health 
        self.energy = energy
    
    def damage(self, damage: int):
        self.health -= damage
        return f"{self.nickname} took {damage}hp damage, health is now {self.health}hp"
    
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
    
    def heal_hp(self):
        raise NotImplementedError
        