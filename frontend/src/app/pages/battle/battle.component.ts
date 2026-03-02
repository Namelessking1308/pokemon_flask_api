import { Component, OnInit } from '@angular/core';
import { Pokemon, PokemonService, CombatResult } from '../../services/pokemon.service';

@Component({
  selector: 'app-battle',
  templateUrl: './battle.component.html',
  styleUrls: ['./battle.component.css']
})
export class BattleComponent implements OnInit {

  pokemons: Pokemon[] = [];
  pagedPokemons: Pokemon[] = [];
  page = 0;
  pageSize = 100;

  selected1?: Pokemon;
  selected2?: Pokemon;
  result?: CombatResult;

  selectingPlayer: 1 | 2 = 1;

  constructor(private pokemonService: PokemonService) {}

  ngOnInit(): void {
    this.pokemonService.getPokemons().subscribe({
      next: (data) => {
        this.pokemons = data;
        this.updatePagedPokemons();
      },
      error: (err) => console.error('Erreur récupération Pokémon:', err)
    });
  }

  updatePagedPokemons() {
    const start = this.page * this.pageSize;
    this.pagedPokemons = this.pokemons.slice(start, start + this.pageSize);
  }

  nextPage() {
    if ((this.page + 1) * this.pageSize < this.pokemons.length) {
      this.page++;
      this.updatePagedPokemons();
    }
  }

  prevPage() {
    if (this.page > 0) {
      this.page--;
      this.updatePagedPokemons();
    }
  }

  selectPokemon(p: Pokemon) {
    if (this.selectingPlayer === 1) {
      this.selected1 = p;
      this.selectingPlayer = 2;
    } else {
      this.selected2 = p;
      this.selectingPlayer = 1;
    }
  }

  startBattle() {
    if (!this.selected1 || !this.selected2) {
      alert('Veuillez sélectionner deux Pokémon !');
      return;
    }

    this.pokemonService.battle(this.selected1.id, this.selected2.id).subscribe({
      next: (res) => this.result = res,
      error: (err) => console.error('Erreur combat:', err)
    });
  }
}