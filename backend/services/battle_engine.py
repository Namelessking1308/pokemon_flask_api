import random

class BattleEngine:

    def __init__(self, pokemon1, pokemon2):
        self.p1 = pokemon1
        self.p2 = pokemon2

        self.p1_hp = pokemon1.hp
        self.p2_hp = pokemon2.hp

        self.logs = []

    def calculate_damage(self, attacker, defender):
        base_damage = ((attacker.attack * 40) / defender.defense) + 2
        random_factor = random.uniform(0.85, 1)
        damage = int(base_damage * random_factor)
        return max(1, damage)

    def fight(self):
        turn = 1

        if self.p1.attack > self.p2.attack:
            first, second = self.p1, self.p2
            first_hp, second_hp = "p1_hp", "p2_hp"
        elif self.p2.attack > self.p1.attack:
            first, second = self.p2, self.p1
            first_hp, second_hp = "p2_hp", "p1_hp"
        else:
            if random.choice([True, False]):
                first, second = self.p1, self.p2
                first_hp, second_hp = "p1_hp", "p2_hp"
            else:
                first, second = self.p2, self.p1
                first_hp, second_hp = "p2_hp", "p1_hp"

        while self.p1_hp > 0 and self.p2_hp > 0:
            damage = self.calculate_damage(first, second)
            setattr(self, second_hp, getattr(self, second_hp) - damage)
            self.logs.append({
                "turn": turn,
                "attacker": first.name,
                "damage": damage,
                "remaining_hp": getattr(self, second_hp)
            })
            if getattr(self, second_hp) <= 0:
                return first, turn, self.logs

            damage = self.calculate_damage(second, first)
            setattr(self, first_hp, getattr(self, first_hp) - damage)
            self.logs.append({
                "turn": turn,
                "attacker": second.name,
                "damage": damage,
                "remaining_hp": getattr(self, first_hp)
            })
            if getattr(self, first_hp) <= 0:
                return second, turn, self.logs

            turn += 1