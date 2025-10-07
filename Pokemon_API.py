import requests
#Basic pokemon api experiment
api_url = "https://pokeapi.co/api/v2/"

def get_pokemon(name):
    url = f"{api_url}/pokemon/{name}"
    response = requests.get(url)
    
    if  response.status_code == 200:
        print("Data retrieved")
        pokedata = response.json()
        return pokedata
    else:
        print("Failed to print data")

#Enter pokemon name to get ID through api
pokemon_name = ""
pokeinfo = get_pokemon(pokemon_name)

if  pokeinfo:
    print(f"{pokeinfo["name"]}")