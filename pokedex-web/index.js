let pokemon_name;


document.getElementById("submit").onclick = async function(){
    pokemon_name = document.getElementById("search").value;

    const api_url = "https://pokeapi.co/api/v2/pokemon/".concat(pokemon_name).toLowerCase();
    
    let response = await fetch(api_url);
    const pokemon_data = await response.json();

    const pokemon_info = {
        "name" : pokemon_data.name,
        "abilities" : pokemon_data.abilities.map(ability_data => ability_data.ability.name),
        "types" : pokemon_data.types.map(type_data => type_data.type.name),
        "base_stats" : pokemon_data.stats.map(stat => stat.base_stat),
        "effort" : pokemon_data.stats.filter(ev => ev.effort > 0).map(ev => [ev.effort, ev.stat.name]),
        "sprite" : pokemon_data.sprites.front_default,
    }

    let texts = document.getElementsByClassName("data");
    console.log("test branch");
    // figureout how foreach work
    let i = 0;
    texts.forEach(element => {
        element.innerText = pokemon_info[keys[i]];
        i++;
    });
}


