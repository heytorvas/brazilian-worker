import { Component, OnInit } from '@angular/core';
import { NgForm } from '@angular/forms';
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

    constructor(private salaryService: LiquidSalaryService) { }

    ngOnInit() {
        this.salary.dependents = 0;
        this.salary.transport_voucher = false;
    }

    numberOnly(event): boolean {
        const charCode = (event.which) ? event.which : event.keyCode;
        if (charCode > 31 && (charCode < 48 || charCode > 57)) {
            return false;
        }
        return true;
    }

    _removeUndefined(obj: Object) {
        Object.keys(obj).forEach(key => obj[key] === undefined && delete obj[key]);
        return obj
    }

    onSubmit(form: NgForm) {
        this.response = null;
        let data = this._removeUndefined(form.value)
        this.salaryService.getSalary(data).subscribe((result) => {
            this.response = result
        })
    }

}