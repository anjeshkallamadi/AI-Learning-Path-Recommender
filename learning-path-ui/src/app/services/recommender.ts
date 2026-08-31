import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class RecommenderService {
  // This points to your local Django server
  private apiUrl = 'http://localhost:8000/api/generate/';

  constructor(private http: HttpClient) { }

  generatePath(chatMessage: string): Observable<any> {
    // We send a JSON object matching what Django expects: {"chat_message": "..."}
    const payload = { chat_message: chatMessage };
    return this.http.post<any>(this.apiUrl, payload);
  }
}