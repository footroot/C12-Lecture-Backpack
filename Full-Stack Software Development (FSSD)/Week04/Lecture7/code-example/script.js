const pokemonInput = document.getElementById('pokemonInput');
const pokemonCard = document.getElementById('pokemonCard');


async function searchPokemon() {

    try {
        const pokemonName = pokemonInput.value.toLowerCase();

        const response = await fetch(`https://pokeapi.co/api/v2/pokemon/${pokemonName}`);

        console.log(response);

        const data = await response.json();

        displayData(data);
    } catch (error) {
        console.log(Error);
    }
}

function displayData(pokemon) {
    pokemonCard.innerHTML = `
        <h2>${pokemon.name.toUpperCase()}</h2>
        <img src="${pokemon.sprites}">
    `
}