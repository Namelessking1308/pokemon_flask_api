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
}

@Injectable({
  providedIn: 'root'
})
export class PokemonService {
  private apiUrl = 'http://localhost:5000';

  constructor(private http: HttpClient) { }

  getPokemons(): Observable<Pokemon[]> {
    return this.http.get<Pokemon[]>(`${this.apiUrl}/pokemons`);
  }

  getPokemonByName(name: string): Observable<Pokemon> {
    return this.http.get<Pokemon>(`${this.apiUrl}/pokemon/${name}`);
  }

  battle(pokemon1_id: number, pokemon2_id: number): Observable<CombatResult> {
    return this.http.post<CombatResult>(`${this.apiUrl}/combat`, {
      pokemon1_id,
      pokemon2_id
    });
  }
}