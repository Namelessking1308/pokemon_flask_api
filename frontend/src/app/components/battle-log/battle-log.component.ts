import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-battle-log',
  templateUrl: './battle-log.component.html',
  styleUrls: ['./battle-log.component.css']
})
export class BattleLogComponent {
  @Input() logs: string[] = [];  // on reçoit les logs du combat
}