import json
import requests

class Pokemon:
    """
    Represents a Pokemon with stats fetched from the PokeAPI.
    """

    def __init__(self, name):
        # Initiation a Pokemon by fetching its data from the API and calculating its stats.
        
        # Args:
        # name (str): The name of the Pokemon (e.g., "pikachu")
        
        # TODO: Store the Pokemon's name (lowercase) [1, 2]
        self.name = name.lower()

        # TODO: Fetch Pokemon data from PokeAPI [1, 3, 4]
        # Create the URL: f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
        # Make GET request
        # Check response status code (raise error if not 200)
        # Store the JSON data
        url = f"https://pokeapi.co/api/v2/pokemon/{self.name}"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
        else:
            print("Get request was unsuccessful")
            return

        # TODO: Calculate and store stats [1, 4-6]
        # Use _calculate_stat() for attack, defense, speed
        # Use _calculate_hp() for max HP
        # Store stats in a dictionary
        # set current_hp to max_hp
        stat_data = data['stats']
        for item in stat_data:
            if item['stat']['name'] == "hp":
                self.max_hp = self._calculate_hp(item['base_stat'])
            elif item['stat']['name'] == "attack":
                self.attack = self._calculate_stat(item['base_stat'])
            elif item['stat']['name'] == "defense":
                self.defense = self._calculate_stat(item['base_stat'])
            elif item['stat']['name'] == "special-attack":
                self.special_attack = self._calculate_stat(item['base_stat'])
            elif item['stat']['name'] == "special-defense":
                self.special_defense = self._calculate_stat(item['base_stat'])
            elif item['stat']['name'] == "speed":
                self.speed = self._calculate_stat(item['base_stat'])
            else:
                print("error")
        
        self.current_hp = self.max_hp

    def _calculate_stat(self, base_stat, level=50, iv=31, ev=0):
        """
        Calculate a Pokemon's stat at a given level.
        Helper method (note the underscore prefix).

        Args:
            base_stat (int): The base stat value from the API
            level (int): Pokemon level (default 50)
            iv (int): Individual value (default 31)
            ev (int): Effort value (default 0)
        Returns:
            int: The calculated stat
        """
        # TODO: Implement the stat calculation formula [7]
        # formula: int(((2 * base_stat + iv + (ev // 4)) * level / 100) + 5)
        stat = int(((2 * base_stat + iv + (ev // 4)) * level / 100) + 5)
        return stat

    def _calculate_hp(self, base_stat, level=50, iv=31, ev=0):
        """
        Calculate a Pokemon's HP at a given level.
        HP uses a different formula than other stats.

        Args:
            base_stat (int): The base HP value from the API
            level (int): Pokemon level (default 50)
            iv (int): Individual value (default 31)
            ev (int): Effort value (default 0)
        Returns:
            int: The calculated HP
        """
        # TODO: Implement the HP calculation formula [7, 8]
        # formula: int(((2 * base_stat + iv + (ev // 4)) * level / 100) + level + 10)
        hp = int(((2 * base_stat + iv + (ev // 4)) * level / 100) + level + 10)
        return hp

    def attack_opponent(self, opponent):
        """
        Attack another Pokemon, dealing damage based on stats.

        Args:
            opponent (Pokemon): The Pokemon being attacked
        Returns:
            int: The amount of damage dealt
        """
        # TODO: calculate damage using the damage formula [8, 9]
        # formula: int((((2 * 50 / 5 + 2) * self.attack * 60 / (opponent.defense * 50)) + 2))
        # 50 is level and 60 is base power
        damage = int((((2 * 50 / 5 + 2) * self.attack * 60 / (opponent.defense * 50)) + 2))
        
        # TODO: Have the defender take damage
        # call opponent.take_damage(damage) [8, 9]
        opponent.take_damage(damage)
        return damage

    def take_damage(self, amount):
        """
        Reduce this Pokemon's HP by the damage amount.

        Args:
            amount (int): The damage to take
        """
        self.current_hp -= amount
        if self.current_hp < 0:
            self.current_hp = 0
        print(f"{self.name} took {amount} damage!") [9, 10]

    def is_fainted(self):
        """
        Check if this Pokemon has fainted (HP <= 0).

        Returns:
            bool: True if fainted, False otherwise
        """
        if self.current_hp <= 0:
            verdict = True
        else:
            verdict = False
        return verdict [10-12]

    def __str__(self):
        """
        String representation of the Pokemon for printing.

        Returns:
            str: A nice display of the Pokemon's name and HP
        """
        # TODO: Return a string like "Pikachu (HP: 95/120)" [10-12]
        return f"{self.name.capitalize()} (HP: {self.current_hp}/{self.max_hp})"

def simulate_battle(pokemon1_name, pokemon2_name):
    """
    Simulate a turn-based battle between two Pokemon.

    Args:
        pokemon1_name (str): Name of the first Pokemon
        pokemon2_name (str): Name of the second Pokemon
    """
    # TODO: Create two Pokemon objects [11, 13]
    pokemon1 = Pokemon(pokemon1_name)
    pokemon2 = Pokemon(pokemon2_name)

    # TODO: Display battle start message [13]
    # show both Pokemon names and initial HP
    print(f"This is a fierce battle between {pokemon1.name} and {pokemon2.name}!")
    print(pokemon1)
    print(pokemon2)

    # TODO: Determine who attacks first based on speed [13, 14]
    # the Pokemon with higher speed goes first
    if pokemon1.speed >= pokemon2.speed:
        winner = pokemon1
        defender = pokemon2
        print(f"{winner.name} attacks first!")
    else:
        winner = pokemon2
        defender = pokemon1
        print(f"{winner.name} attacks first!")

    # Battle loop [14, 15]
    # keep track of round number
    # while neither Pokemon is fainted
    # Display round number
    # Attacker attacks defender
    # Display damage and remaining HP
    # Check if defender fainted
    # if not, swap attacker and defender
    # increment round number
    i = 1
    while pokemon1.is_fainted() == False and pokemon2.is_fainted() == False:
        print(f"--- Round {i} ---")
        if i % 2 != 0:
            print(f"{winner.name} is now attacking!")
            winner.attack_opponent(defender)
            print(winner)
            print(defender)
            i = i + 1
        else:
            print(f"{defender.name} is now attacking!")
            defender.attack_opponent(winner)
            print(defender)
            print(winner)
            i = i + 1

    print("\nThe match has ended!") [15]
    if pokemon1.is_fainted() == False:
        print(f"The winning pokemon is {pokemon1.name} with HP: {pokemon1.current_hp}")
    else:
        print(f"The winning pokemon is {pokemon2.name} with HP: {pokemon2.current_hp}")

if __name__ == "__main__":
    # Test your battle simulator [15]
    simulate_battle("pikachu", "bulbasaur")
    
    # Uncomment to test other battles
    # simulate_battle("vulpix", "horsea")
    # simulate_battle("mew", "mewtwo")
