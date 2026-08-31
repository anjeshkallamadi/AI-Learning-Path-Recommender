import { Component , Input} from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-roadmap',
  standalone: true,
  imports: [CommonModule],
  styleUrl: './roadmap.css',
  templateUrl: './roadmap.html',
})
export class Roadmap {
  @Input() pathData: any = null;
}
