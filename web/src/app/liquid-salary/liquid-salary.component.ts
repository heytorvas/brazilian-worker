import { Component, OnInit } from '@angular/core';
import { NgForm } from '@angular/forms';
import { AppComponent } from '../app.component';
import { LiquidSalary, Salary } from './liquid-salary.model';
import { LiquidSalaryService } from './liquid-salary.service';

@Component({
    selector: 'app-liquid-salary',
    templateUrl: './liquid-salary.component.html',
    styleUrls: ['./liquid-salary.component.css']
})

export class LiquidSalaryComponent implements OnInit {

    salary: LiquidSalary = {} as LiquidSalary;
    response!: Salary | null;

    loading: boolean = false;

    constructor(private salaryService: LiquidSalaryService, private app: AppComponent) { }

    ngOnInit() {
        this.salary.dependents = 0;
        this.salary.transport_voucher = false;
    }

    _removeUndefined(obj: Object) {
        return this.app.removeUndefined(obj);
    }

    numberOnly(event) {
        return this.app.numberOnly(event);
    }

    onSubmit(form: NgForm) {
        this.loading = true;
        this.response = null;
        let data = this._removeUndefined(form.value)
        this.salaryService.getSalary(data).subscribe((result) => {
            this.loading = false;
            this.response = result
        })
    }

}