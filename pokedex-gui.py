from tkinter import *
import requests
from PIL import Image, ImageTk
from io import BytesIO
import vlc

root = Tk()
root.title("Pokedex by Carlo")

frame = Frame(root)
frame.grid(row=0)

top_most = False
def top(event):
    global top_most
    
    if event.keysym == "F8" and top_most == False:
        root.attributes("-topmost", True)
        print("nice")
        top_most = True
    elif event.keysym == "F8" and top_most == True:
        root.attributes("-topmost", False)
        print("not nice")
        top_most = False

def Search_Pokemon(_):
    global pokemon_info

    url = f"https://pokeapi.co/api/v2/pokemon/{search_bar.get().lower()}"
    response = requests.get(url)
    
    if response.status_code == 200:
        pokemon_data = response.json()
        pokemon_info = {
            "name": pokemon_data["name"],
            "abilities": [ability["ability"]["name"] for ability in pokemon_data["abilities"]],
            "types": [type_data["type"]["name"] for type_data in pokemon_data["types"]],
            "base_stats" : [stats["base_stat"] for stats in pokemon_data["stats"]],
            "effort" : [(ev["effort"], ev["stat"]["name"]) for ev in pokemon_data["stats"] if ev["effort"] > 0],
            "sprite" : pokemon_data["sprites"]["front_default"],
            "cry" : pokemon_data["cries"]["latest"]
        }
        DisplayData(True)
    else:
        DisplayData(False, None)

def DisplayData(state):
    global img_ref # apparently if PhotoImage is not referenced, garbage collector may remove it
    
    for widget in frame.winfo_children():
        if widget != search_bar:
            widget.destroy()
    
    if state == True:
        name = Label(frame, text=f"Name: {pokemon_info['name']}")
        abilities = Label(frame, text=f"Abilities: {', '.join(pokemon_info['abilities'])}")
        types = Label(frame, text=f"Types: {', '.join(pokemon_info['types'])}")
        #region Stats
        hp = Label(frame, text=f"HP: {pokemon_info["base_stats"][0]}")
        atk = Label(frame, text=f"ATK: {pokemon_info["base_stats"][1]}")
        defs = Label(frame, text=f"DEF: {pokemon_info["base_stats"][2]}")
        spatk = Label(frame, text=f"SPATK: {pokemon_info["base_stats"][3]}")
        spdef =Label(frame, text=f"SPDEF: {pokemon_info["base_stats"][4]}")
        spd = Label(frame, text=f"SPD: {pokemon_info["base_stats"][5]}")
        total = Label(frame, text=f"TOTAL: {sum(pokemon_info["base_stats"])}")
        #endregion
        ev_yield_str = ', '.join(f"{effort} {stat}" for effort, stat in pokemon_info['effort'])
        ev_yield = Label(frame, text=f"EV Yield: {ev_yield_str}")
        

        img_url_response = requests.get(pokemon_info['sprite'])
        img = Image.open(BytesIO(img_url_response.content))
        img_tk = ImageTk.PhotoImage(img)
        
        img_ref = img_tk
        
        img_panel = Button(frame, image = img_tk, command=PlayCry,highlightthickness=0, bd=0)
        
        #region Packs
        name.grid(row=1)
        abilities.grid(row=2)
        types.grid(row=3)
        hp.grid(row=4)
        atk.grid(row=5)
        defs.grid(row=6)
        spatk.grid(row=7)
        spdef.grid(row=8)
        spd.grid(row=9)
        total.grid(row=10)
        ev_yield.grid(row=11)
        img_panel.grid(row=12)
        #endregion
    else:
        error = Label(frame, text="INVALID POKEMON NAME")
        error.grid(row=1)

def PlayCry():
    cry_url = pokemon_info["cry"]
    sound = vlc.MediaPlayer(cry_url)
    sound.play()

        
root.bind('<Return>', Search_Pokemon)

search_bar = Entry(frame, width=41)
search_bar.grid(row=0)

root.bind("<Key>", top)
root.mainloop()