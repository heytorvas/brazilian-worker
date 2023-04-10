import { Component, OnInit } from '@angular/core';
import { NgForm } from '@angular/forms';
import { AppComponent } from '../../app.component';
import { AppService } from '../../app.service';
import { PJSalary, PJSalaryBase } from './pj-salary.model';
import { ERROR_MESSAGES } from '../../app.service';

@Component({
  selector: 'app-pj-salary',
  templateUrl: './pj-salary.component.html',
  styleUrls: ['./pj-salary.component.css']
})
export class PjSalaryComponent implements OnInit {

  salary: PJSalaryBase = {} as PJSalaryBase;
  response!: PJSalary | null;
  loading: boolean = false;
  errorEnabled = false;
  errorMessage = '';

  constructor(private appService: AppService, private app: AppComponent) { }

  ngOnInit(): void {
    this.salary.attachment = 'I';
  }

  numberOnly(event) {
    this.app.numberOnly(event);
  }

  onSubmit(form: NgForm) {
    this.loading = true;
    this.response = null;
    this.appService.requestData('pj', this.app.removeUndefined(form.value)).subscribe((result) => {
      this.loading = false;
      this.response = result;
    }, (error) => {
      this.response = null;
      this.loading = false;
      this.errorEnabled = true;
      this.errorMessage = ERROR_MESSAGES[error.error.error.message];
    })
  }
}
