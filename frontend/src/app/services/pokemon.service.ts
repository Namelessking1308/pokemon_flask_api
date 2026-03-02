import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface Pokemon {
  id: number;
  name: string;
  hp: number;
  attack: number;
  defense: number;
  sprite_url: string;
}

export interface CombatResult {
  winner: string;
  turns: number;
  logs: string[];
  hp1: number;
  hp2: number;
}

@Injectable({
  providedIn: 'root'
})
export class PokemonService {
  private apiUrl = 'http://127.0.0.1:5000';

  constructor(private http: HttpClient) {}

  getPokemons(): Observable<Pokemon[]> {
    return this.http.get<Pokemon[]>(`${this.apiUrl}/pokemons`);
  }

  battle(pokemon1Id: number, pokemon2Id: number): Observable<CombatResult> {
    return this.http.post<CombatResult>(`${this.apiUrl}/battle`, {
      pokemon1_id: pokemon1Id,
      pokemon2_id: pokemon2Id
    });
  }
}