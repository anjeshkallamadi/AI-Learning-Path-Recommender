import { TestBed } from '@angular/core/testing';
import { Recommender } from './recommender';

describe('Recommender', () => {
  let service: Recommender;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(Recommender);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
