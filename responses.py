import random
from typing import Dict

def add_character(characters: Dict[str, Dict[str, int]], name: str, str_stat: int, dex_stat: int, con_stat: int, int_stat: int, wis_stat: int, cha_stat: int) -> str:
    if name in characters:
        return f"A character named {name} already exists."
    else:
        characters[name] = {
            "STR": str_stat,
            "DEX": dex_stat,
            "CON": con_stat,
            "INT": int_stat,
            "WIS": wis_stat,
            "CHA": cha_stat
        }
        return f"Character {name} added successfully!"

def check_character_stats(characters: Dict[str, Dict[str, int]], name: str) -> str:
    if name in characters:
        stats = characters[name]
        stats_display = "\n".join([f"{stat}: {value}" for stat, value in stats.items()])
        return f"Stats for {name}:\n{stats_display}"
    else:
        return f"No character named {name} found."

def delete_character(characters: Dict[str, Dict[str, int]], name: str) -> str:
    if name in characters:
        del characters[name]
        return f"Character {name} has been deleted."
    else:
        return f"No character named {name} found."

def display_all_characters(characters: Dict[str, Dict[str, int]]) -> str:
    if not characters:
        return "No characters stored."
    else:
        all_characters = ""
        for character_name, stats in characters.items():
            stats_display = "\n".join([f"{stat}: {value}" for stat, value in stats.items()])
            all_characters += f"Name: {character_name}\n{stats_display}\n\n"
        return all_characters

def roll_d20_for_character_stat(characters: Dict[str, Dict[str, int]], name: str, stat_name: str) -> str:
    if name in characters:
        if stat_name.upper() in characters[name]:
            stat_value = characters[name][stat_name.upper()]
            roll_result = random.randint(1, 20)
            final_result = roll_result + stat_value
            return f"{name} rolled a d20 and got: {roll_result}\nUsing {stat_name.upper()} ({stat_value}), the final result is: {final_result}"
        else:
            return f"{name} does not have a stat called {stat_name}."
    else:
        return f"No character named {name} found."
