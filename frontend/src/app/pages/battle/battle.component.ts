import { Component, OnInit } from '@angular/core';
import { PokemonService, Pokemon, CombatResult } from '../../services/pokemon.service';

@Component({
  selector: 'app-battle',
  templateUrl: './battle.component.html',
  styleUrls: ['./battle.component.css']
})
export class BattleComponent implements OnInit {

  pokemons: Pokemon[] = [];

  player1Selected?: Pokemon;
  player2Selected?: Pokemon;

  result?: CombatResult;

  hp1Percent = 100;
  hp2Percent = 100;

  inCombat = false;

  constructor(private pokemonService: PokemonService) {}

  ngOnInit(): void {
    this.pokemonService.getPokemons().subscribe(data => {
      this.pokemons = data;
    });
  }
  selectPlayer1(p: Pokemon) {
  this.player1Selected = p;
  this.resetBattleState();
  }

  selectPlayer2(p: Pokemon) {
  this.player2Selected = p;
  this.resetBattleState();
  }

  startBattle() {
    if (!this.player1Selected || !this.player2Selected) return;

    this.resetBattleState();
    
    this.pokemonService
      .battle(this.player1Selected.id, this.player2Selected.id)
      .subscribe(res => {
        this.result = res;
        this.hp1Percent = 100;
        this.hp2Percent = 100;
        this.animateBattle();
      });
  }

  resetBattleState() {
  this.result = undefined;
  this.hp1Percent = 100;
  this.hp2Percent = 100;
  this.inCombat = false;
}

  animateBattle() {
  if (!this.result || !this.player1Selected || !this.player2Selected) return;

  this.inCombat = true;

  const p1 = this.player1Selected;
  const p2 = this.player2Selected;
  const logs = this.result.logs;

  let index = 0;

  const interval = setInterval(() => {

    if (index >= logs.length) {
      clearInterval(interval);
      this.inCombat = false;
      return;
    }

    const log = logs[index];

    this.hp1Percent = (log.hp1 / p1.hp) * 100;
    this.hp2Percent = (log.hp2 / p2.hp) * 100;

    const img1 = document.getElementById('p1-img');
    const img2 = document.getElementById('p2-img');

    if (log.attacker === p1.name) {
      img1?.classList.add('attack');
    } else {
      img2?.classList.add('attack');
    }

    setTimeout(() => {
      img1?.classList.remove('attack');
      img2?.classList.remove('attack');
    }, 300);

    index++;

  }, 800);
}}