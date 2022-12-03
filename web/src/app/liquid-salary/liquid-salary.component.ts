import { Component, OnInit } from '@angular/core';
import { NgForm } from '@angular/forms';
import { LiquidSalary, Salary } from './liquid-salary.model';
import { HttpClient } from '@angular/common/http';
import { API } from '../app.api';
import { LiquidSalaryService } from './liquid-salary.service';

@Component({
    selector: 'app-liquid-salary',
    templateUrl: './liquid-salary.component.html',
    styleUrls: ['./liquid-salary.component.css']
})

export class LiquidSalaryComponent implements OnInit {

    salary: LiquidSalary = {} as LiquidSalary;
    response!: Salary

    constructor(private salaryService: LiquidSalaryService) { }

    ngOnInit() {

    }

    numberOnly(event): boolean {
        const charCode = (event.which) ? event.which : event.keyCode;
        if (charCode > 31 && (charCode < 48 || charCode > 57)) {
            return false;
        }
        return true;

    }

    onSubmit(form: NgForm) {
        console.log(form.value);
    }

    test() { 
        let data = {"raw": 2222};
        this.salaryService.getSalary(data).subscribe((result) => {
            this.response = result
            console.log(this.response)
        })
    }


}