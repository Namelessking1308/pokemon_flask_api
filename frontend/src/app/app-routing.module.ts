import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { PokemonsComponent } from './pages/pokemons/pokemons.component';
import { BattleComponent } from './pages/battle/battle.component';

const routes: Routes = [
  { path: '', redirectTo: '/pokemons', pathMatch: 'full' }, // page d'accueil
  { path: 'pokemons', component: PokemonsComponent },
  { path: 'battle', component: BattleComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }