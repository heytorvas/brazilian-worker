import { Component, OnInit } from '@angular/core';
import { NgForm } from '@angular/forms';
import { AppComponent } from '../../app.component';
import { CLTSalary, CLTSalaryBase } from './clt-salary.model';
import { AppService } from '../../app.service';
import { ERROR_MESSAGES } from '../../app.service';

@Component({
    selector: 'app-clt-salary',
    templateUrl: './clt-salary.component.html',
    styleUrls: ['./clt-salary.component.css']
})

export class CLTSalaryComponent implements OnInit {

    salary: CLTSalary = {} as CLTSalary;
    response!: CLTSalaryBase | null;
    dependents;
    loading: boolean = false;
    errorEnabled = false;
    errorMessage = '';

    constructor(private appService: AppService, private app: AppComponent) { }

    ngOnInit() {
        this.salary.dependents = 0;
        this.salary.transport_voucher = false;
        this.dependents = this.app.dependents;
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
        this.appService.requestData('clt', data).subscribe((result) => {
            this.loading = false;
            this.response = result
        }, (error) => {
            this.response = null;
            this.loading = false;
            this.errorEnabled = true;
            this.errorMessage = ERROR_MESSAGES[error.error.error.message];
        })
    }

}