import { Component, OnInit } from '@angular/core';
import { NgForm } from '@angular/forms';
import { AppComponent } from '../../app.component';
import { CompareOutputSchema } from '../../shared/compare.model';
import { PJSalaryBase } from '../pj-salary/pj-salary.model';
import { AppService, ERROR_MESSAGES } from '../../app.service';

@Component({
  selector: 'app-pj-clt',
  templateUrl: './pj-clt.component.html',
  styleUrls: ['./pj-clt.component.css']
})
export class PjCltComponent implements OnInit {

  salary: PJSalaryBase = {} as PJSalaryBase;
  response!: CompareOutputSchema | null;
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
    this.appService.requestData('compare/pj', form.value).subscribe((result) => {
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
