import { Component, OnInit } from '@angular/core';
import { NgForm } from '@angular/forms';
import { AppComponent } from '../../app.component';
import { AppService, ERROR_MESSAGES } from '../../app.service';
import { Thirteenth } from './thirteenth.model';

@Component({
  selector: 'app-thirteenth',
  templateUrl: './thirteenth.component.html',
  styleUrls: ['./thirteenth.component.css']
})
export class ThirteenthComponent implements OnInit {

  salary: Thirteenth = {} as Thirteenth;
  response!: Thirteenth | null;
  months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
  errorEnabled = false;
  errorMessage = '';
  loading: boolean = false;
  dependents;

  constructor(private appService: AppService, private app: AppComponent) { }

  ngOnInit(): void {
    this.salary.dependents = 0;
    this.salary.months = 12;
    this.dependents = this.app.dependents;
  }

  numberOnly(event) {
    this.app.numberOnly(event);
  }

  onSubmit(form: NgForm) {
    this.loading = true;
    this.response = null;
    this.appService.requestData('thirteenth', this.app.removeUndefined(form.value)).subscribe((result) => {
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
