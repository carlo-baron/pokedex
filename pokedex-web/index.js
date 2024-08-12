let pokemon_name;


document.getElementById("submit").onclick = async function(e){
    e.preventDefault();

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
        "cry" : pokemon_data.cries.latest
    }

    let texts = document.getElementsByClassName("data");
    var textsArr = [].slice.call(texts);

    textsArr[0].innerText = pokemon_info.name;
    textsArr[1].innerText = pokemon_info.abilities;
    textsArr[2].innerText = pokemon_info.types;
    textsArr[3].innerText = pokemon_info.base_stats;
    textsArr[4].innerText = pokemon_info.base_stats.reduce((sum, a) => sum + a);
    textsArr[5].innerText = pokemon_info.effort;

    var audio = document.querySelector("audio");

    document.getElementById("sprite").src = pokemon_info.sprite;
    document.getElementById("cry").src = pokemon_info.cry;

    audio.load();
}


