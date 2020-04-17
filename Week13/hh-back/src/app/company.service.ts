import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Company, LoginResponse, Vacancy} from './model';
import {Observable} from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class CompanyService {
  BASE_URL = 'http://127.0.0.1:8000';

  constructor(private http: HttpClient) {
  }

  getCompanyList(): Observable<Company[]> {
    return this.http.get<Company[]>(`${this.BASE_URL}/api/companies/`);

  }

  getCompanyVacancyList(id: number): Observable<Vacancy[]> {
    return this.http.get<Vacancy[]>(`${this.BASE_URL}/api/companies/${id}/vacancies/`);
  }

  login(username, password): Observable<LoginResponse> {
    return this.http.post<LoginResponse>(`${this.BASE_URL}/api/login/`, {
      username,
      password
    });
  }
}

