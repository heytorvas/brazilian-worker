import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from 'src/environments/environment';

@Injectable({
    providedIn: 'root'
})
export class AppService {
    constructor(private http: HttpClient) { }

    requestData(endpoint, data) {
        const headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
        };
        return this.http.post<any>(`${environment.API}/${endpoint}`, data, { headers });
    }
}

export const ERROR_MESSAGES = {
    'Maximum CLT raw salary reached.': 'Máximo salário bruto da CLT atingido. Verifique o valor informado e tente novamente.',
    'Maximum PJ raw salary reached.': 'Máximo salário bruto da PJ atingido. Verifique o valor informado e tente novamente.',
    'Internal Server Error.': 'Erro interno do servidor. Tente novamente mais tarde.',
}