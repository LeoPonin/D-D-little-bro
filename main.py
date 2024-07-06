from typing import Final, Dict
import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
import responses

# Load the token
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

# Bot setup
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='#', intents=intents)

# Global dictionary to store characters
characters: Dict[str, Dict[str, int]] = {}

@bot.command(name='hello')
async def hello(ctx):
    await ctx.send(f"Hello, {ctx.author.name}! #add name STR DEX CON INT WIS CHA Adds a new character with the given stats. Example: `#add Bob 10 12 14 8 16 18`\n #check name Displays the stats of the specified character.Example: `#check Bob`\n #delete name Deletes the specified character.Example: `#delete Bob`\n #list Lists all stored characters and their stats. \n #roll name stat Rolls a d20 and adds the result to the specified stat of the character.Example: `#roll Bob STR`")
        
# Command to add a new character
@bot.command(name='add')
async def add_character(ctx, name: str, str_stat: int, dex_stat: int, con_stat: int, int_stat: int, wis_stat: int, cha_stat: int):
    response = responses.add_character(characters, name, str_stat, dex_stat, con_stat, int_stat, wis_stat, cha_stat)
    await ctx.send(response)

# Command to check character's stats
@bot.command(name='check')
async def check_character_stats(ctx, name: str):
    response = responses.check_character_stats(characters, name)
    await ctx.send(response)

# Command to delete a character
@bot.command(name='delete')
async def delete_character(ctx, name: str):
    response = responses.delete_character(characters, name)
    await ctx.send(response)

# Command to display all characters
@bot.command(name='list')
async def display_all_characters(ctx):
    response = responses.display_all_characters(characters)
    await ctx.send(response)

# Command to roll a d20 for a character stat
@bot.command(name='roll')
async def roll_d20_for_character_stat(ctx, name: str, stat_name: str):
    response = responses.roll_d20_for_character_stat(characters, name, stat_name)
    await ctx.send(response)

# Command to exit the bot (for demonstration, typically not included in production bots)
@bot.command(name='exit')
async def exit_bot(ctx):
    await ctx.send("Exiting bot...")
    await bot.close()

# Run the bot
bot.run(TOKEN)
