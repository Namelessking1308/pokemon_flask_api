import { Component, OnInit } from '@angular/core';
import { PokemonService, Pokemon } from '../../services/pokemon.service';

@Component({
  selector: 'app-pokemons',
  templateUrl: './pokemons.component.html',
  styleUrls: ['./pokemons.component.css']
})
export class PokemonsComponent implements OnInit {
  pokemons: Pokemon[] = [];

  constructor(private pokemonService: PokemonService) {}

  ngOnInit(): void {
    this.pokemonService.getPokemons().subscribe({
      next: (data) => {
        console.log(data); // pour vérifier les URLs
        this.pokemons = [...data]; // force Angular à détecter le tableau
      },
      error: (err) => console.error('Erreur lors de la récupération des Pokémon :', err)
    });
  }
}