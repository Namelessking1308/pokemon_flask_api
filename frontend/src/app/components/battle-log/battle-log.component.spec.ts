import { Component, OnInit } from '@angular/core';
import { Pokemon, PokemonService, CombatResult } from '../../services/pokemon.service';

@Component({
  selector: 'app-battle',
  templateUrl: './battle.component.html',
  styleUrls: ['./battle.component.css']
})
export class BattleComponent implements OnInit {
  pokemons: Pokemon[] = [];
  player1?: Pokemon;
  player2?: Pokemon;
  result?: CombatResult;
  selectingPlayer: number = 1;
  player1HP: number = 0;
  player2HP: number = 0;

  constructor(private pokemonService: PokemonService) {}

  ngOnInit(): void {
    this.pokemonService.getPokemons().subscribe(data => this.pokemons = data);
  }

  selectPokemon(p: Pokemon): void {
    if(this.selectingPlayer === 1){
      this.player1 = {...p};
      this.player1HP = p.hp;
      this.selectingPlayer = 2;
    } else {
      this.player2 = {...p};
      this.player2HP = p.hp;
    }
  }

  startBattle(): void {
    if(!this.player1 || !this.player2) return;

    this.pokemonService.battle(this.player1.id, this.player2.id).subscribe(res => {
      this.result = res;
      this.animateBattle();
    });
  }

  animateBattle(): void {
    // Exemple d'animation simple pour faire diminuer la barre de vie
    if(!this.result || !this.player1 || !this.player2) return;

    const winner = this.result.winner === this.player1.name ? this.player1 : this.player2;
    const loserHP = winner === this.player1 ? this.player2HP : this.player1HP;
    
    // Ici tu peux faire une animation avec setInterval ou un tween pour diminuer la vie
  }
}