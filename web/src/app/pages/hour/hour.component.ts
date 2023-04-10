import { Component, OnInit } from '@angular/core';
import { NgForm } from '@angular/forms';
import { AppComponent } from 'src/app/app.component';
import { AppService, ERROR_MESSAGES } from 'src/app/app.service';
import { Hour, HourBase } from './hour.model';

@Component({
  selector: 'app-hour',
  templateUrl: './hour.component.html',
  styleUrls: ['./hour.component.css']
})
export class HourComponent implements OnInit {
  hour: HourBase = {} as HourBase;
  response!: Hour | null;
  loading: boolean = false;
  errorEnabled = false;
  errorMessage = ERROR_MESSAGES['Default'];

  constructor(private appService: AppService, private app: AppComponent) { }

  ngOnInit(): void {
  }

  numberOnly(event) {
    this.app.numberOnly(event);
  }

  onSubmit(form: NgForm) {
    this.loading = true;
    this.response = null;
    let data = this.app.removeUndefined(form.value)
    this.appService.requestData('hour', data).subscribe((result) => {
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
