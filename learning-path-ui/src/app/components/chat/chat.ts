import { Component, ChangeDetectorRef } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms'; // Needed for ngModel
import { RecommenderService } from '../../services/recommender';
import { Roadmap } from '../roadmap/roadmap';

@Component({
  selector: 'app-chat',
  standalone: true,
  imports: [CommonModule, FormsModule, Roadmap],
  templateUrl: './chat.html',
  styleUrls: ['./chat.css']
})
export class ChatComponent {
  userMessage: string = '';
  isLoading: boolean = false;
  aiResponse: any = null;
  parsedData: any = null; // <-- 1. Add this new variable

  constructor(private recommenderService: RecommenderService ,
    private cdr: ChangeDetectorRef
  ) {}

  sendMessage() {
    if (!this.userMessage.trim()) return;

    this.isLoading = true;
    this.recommenderService.generatePath(this.userMessage).subscribe({
      next: (response) => {
        // The Fix: Push the update to the very end of the execution queue
        setTimeout(() => {
          this.aiResponse = response.ai_response;
          
          // We create a completely fresh object clone using the spread operator {...}
          // This forces Angular to realize the data is brand new.
          this.parsedData = { ...this.parseJSON(this.aiResponse) }; 
          
          this.isLoading = false;
          
          // Force the UI alarm clock to ring
          this.cdr.detectChanges(); 
        }, 0);
      },
      error: (err) => {
        setTimeout(() => {
          console.error("Error connecting to Django:", err);
          this.isLoading = false;
          this.cdr.detectChanges();
        }, 0);
      }
    });
  }

  // Add this method inside your ChatComponent class
parseJSON(responseString: string) {
  try {
    // Sometimes LLMs wrap JSON in markdown blocks like ```json ... ```
    const cleanString = responseString.replace(/```json/g, '').replace(/```/g, '').trim();
    return JSON.parse(cleanString);
  } catch (e) {
    console.error("Failed to parse AI JSON:", e);
    return null;
  }
}
}