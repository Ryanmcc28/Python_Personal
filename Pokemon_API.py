import requests
#Basic pokemon api experiment

print("Enter the name of a Pokemon");
name = input()

api_url = f"https://pokeapi.co/api/v2/pokemon/{name}"

def get_pokemon():
    response = requests.get(api_url)
    if  response.status_code == 200:
        print("Data retrieved")
        pokedata = response.json()

        return pokedata
    else:
        print("Failed to print data")
        print(f"Response code: {response.status_code}")


pokeinfo = get_pokemon()

if pokeinfo:
    id = pokeinfo["id"]
    print(f"ID is: {id}")
    print(f"Name is: {pokeinfo['name']}")
    print(f"Height is: {pokeinfo['height']}")
    print(f"Weight is: {pokeinfo['weight']}")

    # Determine generation
    if 1 <= id <= 151:
        print("Generation 1!")
    elif 152 <= id <= 251:
        print("Generation 2!")
    elif 252 <= id <= 386:
        print("Generation 3!")
    elif 387 <= id <= 493:
        print("Generation 4!")
    elif 494 <= id <= 649:
        print("Generation 5!")
    elif 650 <= id <= 721:
        print("Generation 6!")
    elif 722 <= id <= 809:
        print("Generation 7!")
    elif 810 <= id <= 898:
        print("Generation 8!")
    elif 899 <= id <= 1010:
        print("Generation 9!")
    else:
        print("Generation unknown!")
