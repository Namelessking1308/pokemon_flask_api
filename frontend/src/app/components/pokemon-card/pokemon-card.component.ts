import { Component, Input } from '@angular/core';
import { Pokemon } from '../../services/pokemon.service';

@Component({
  selector: 'app-pokemon-card',
  templateUrl: './pokemon-card.component.html',
  styleUrls: ['./pokemon-card.component.css']
})
export class PokemonCardComponent {
  @Input() pokemon!: Pokemon; // l'objet Pokémon entier est passé depuis le parent
}