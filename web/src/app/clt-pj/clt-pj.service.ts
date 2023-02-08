import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from 'src/environments/environment';

@Injectable({
    providedIn: 'root'
})
export class CLTPJService {

    constructor(private http: HttpClient) { }

    getSalary(data) {
        const headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
        };
        return this.http.post<any>(`${environment.API}/compare/clt`, data, { headers });
    }
}