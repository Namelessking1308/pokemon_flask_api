import { Component, OnInit } from '@angular/core';
import { Pokemon, PokemonService, CombatResult } from '../../services/pokemon.service';

@Component({
  selector: 'app-battle',
  templateUrl: './battle.component.html',
  styleUrls: ['./battle.component.css']
})
export class BattleComponent implements OnInit {
  pokemons: Pokemon[] = [];
  selected1?: Pokemon;
  selected2?: Pokemon;
  result?: CombatResult;

  constructor(private pokemonService: PokemonService) {}

  ngOnInit(): void {
    this.pokemonService.getPokemons().subscribe(data => this.pokemons = data);
  }

  startBattle(): void {
    if (!this.selected1 || !this.selected2) return;

    this.pokemonService.battle(this.selected1.id, this.selected2.id).subscribe(res => {
      this.result = res;
    });
  }
}