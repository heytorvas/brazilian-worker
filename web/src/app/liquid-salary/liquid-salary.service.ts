import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { API } from '../app.api';

@Injectable({
    providedIn: 'root'
})
export class LiquidSalaryService {

    constructor(private http: HttpClient) { }
    
    getSalary(data) {
        const headers = {
            'accept': 'application/json', 
            'Content-Type': 'application/json',
        };
        return this.http.post<any>(`${API}/salary`, data, {headers});
    }
}