import os
import requests
from pathlib import Path
from bs4 import BeautifulSoup

from dex.models import Pokemon

'''
Script to web scrape data for the original 151 Pokemon and put in a database for a Django project

usage (from project dir):
./manage.py shell < get-poke-data.py
'''

####################
# Get Pokemon Images
####################

# make sure static/images dir exists
img_dir = Path('static/images')
if not img_dir.exists():
    img_dir.mkdir(parents=True, exist_ok=True)    

# move on if images alredy has 151 things in it
if len(os.listdir('static/images')) == 151:
    print('static/images already has images for all 151 Pokemon')
else:
    # get images for each pokemon
    images_base_url = 'https://assets.pokemon.com/assets/cms2/img/pokedex/full/'
    print('getting Pokemon images...')
    for n in range(1,152):
        pic = requests.get(f'{images_base_url}/{n:03}.png')
        with open(f'{img_dir}/{n:03}.png', 'wb') as f:
            f.write(pic.content)

##################
# Get Pokemon Info
##################

# check if database already has all 151 Pokemon in it
if len(Pokemon.objects.all()) == 151:
    print('Database already has all 151 Pokemon')
else:
    poke_list = [
        'Bulbasaur', 'Ivysaur', 'Venusaur', 'Charmander', 'Charmeleon', 'Charizard', 'Squirtle', 'Wartortle', 'Blastoise',
        'Caterpie', 'Metapod', 'Butterfree', 'Weedle', 'Kakuna', 'Beedrill', 'Pidgey', 'Pidgeotto', 'Pidgeot', 'Rattata', 
        'Raticate', 'Spearow', 'Fearow', 'Ekans', 'Arbok', 'Pikachu', 'Raichu', 'Sandshrew', 'Sandslash', 'nidoran-female', 
        'Nidorina', 'Nidoqueen', 'nidoran-male', 'Nidorino', 'Nidoking', 'Clefairy', 'Clefable', 'Vulpix', 'Ninetales', 
        'Jigglypuff', 'Wigglytuff', 'Zubat', 'Golbat', 'Oddish', 'Gloom', 'Vileplume', 'Paras', 'Parasect', 'Venonat', 
        'Venomoth', 'Diglett', 'Dugtrio', 'Meowth', 'Persian', 'Psyduck', 'Golduck', 'Mankey', 'Primeape', 'Growlithe', 
        'Arcanine', 'Poliwag', 'Poliwhirl', 'Poliwrath', 'Abra', 'Kadabra', 'Alakazam', 'Machop', 'Machoke', 'Machamp', 
        'Bellsprout', 'Weepinbell', 'Victreebel', 'Tentacool', 'Tentacruel', 'Geodude', 'Graveler', 'Golem', 'Ponyta', 
        'Rapidash', 'Slowpoke', 'Slowbro', 'Magnemite', 'Magneton', 'farfetchd', 'Doduo', 'Dodrio', 'Seel', 'Dewgong', 
        'Grimer', 'Muk', 'Shellder', 'Cloyster', 'Gastly', 'Haunter', 'Gengar', 'Onix', 'Drowzee', 'Hypno', 'Krabby', 
        'Kingler', 'Voltorb', 'Electrode', 'Exeggcute', 'Exeggutor', 'Cubone', 'Marowak', 'Hitmonlee', 'Hitmonchan', 
        'Lickitung', 'Koffing', 'Weezing', 'Rhyhorn', 'Rhydon', 'Chansey', 'Tangela', 'Kangaskhan', 'Horsea', 'Seadra', 
        'Goldeen', 'Seaking', 'Staryu', 'Starmie', 'mr-mime', 'Scyther', 'Jynx', 'Electabuzz', 'Magmar', 'Pinsir', 
        'Tauros', 'Magikarp', 'Gyarados', 'Lapras', 'Ditto', 'Eevee', 'Vaporeon', 'Jolteon', 'Flareon', 'Porygon', 
        'Omanyte', 'Omastar', 'Kabuto', 'Kabutops', 'Aerodactyl', 'Snorlax', 'Articuno', 'Zapdos', 'Moltres', 'Dratini', 
        'Dragonair', 'Dragonite', 'Mewtwo', 'Mew'
    ]

    # get types, height, weight, and description for each pokemon
    base_url = "https://pokemon.com/us/pokedex/"
    print('getting Pokemon info...')
    for index, pokemon in enumerate(poke_list):
        # get web page for Pokemon
        r = requests.get(f"{base_url}/{pokemon}")
        # parse with BeautifulSoup
        soup = BeautifulSoup(r.content, "html.parser")

        # get Pokemon type(s)
        type_info =  soup.find("div", class_="dtm-type").find_all('a')
        type1 = type_info[0].text
        if len(type_info) == 2:
            type2 = type_info[1].text
        else:
            type2 = None 

        # get Pokemon height and weight
        height = soup.find_all("span", class_="attribute-value")[0].text
        weight = soup.find_all("span", class_="attribute-value")[1].text

        # get Pokemon description
        description = soup.find("p", class_="version-x").text.strip()

        # put Pokemon data in database
        pokemon_obj = Pokemon(number=index + 1, name=pokemon, type1=type1, type2=type2, height=height, weight=weight, description=description)
        pokemon_obj.save()

