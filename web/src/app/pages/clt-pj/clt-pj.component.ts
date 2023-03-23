import { Component, OnInit } from '@angular/core';
import { NgForm } from '@angular/forms';
import { AppComponent } from '../../app.component';
import { AppService, ERROR_MESSAGES } from '../../app.service';
import { CompareOutputSchema } from '../../shared/compare.model';
import { CLTPJSchema } from './clt-pj.model';

@Component({
  selector: 'app-clt-pj',
  templateUrl: './clt-pj.component.html',
  styleUrls: ['./clt-pj.component.css']
})
export class CltPjComponent implements OnInit {
  salary: CLTPJSchema = {} as CLTPJSchema;
  response!: CompareOutputSchema | null;
  loading: boolean = false;
  errorEnabled = false;
  errorMessage = '';
  dependents;

  constructor(private appService: AppService, private app: AppComponent) { }

  ngOnInit(): void {
    this.salary.dependents = 0;
    this.salary.transport_voucher = false;
    this.salary.attachment = 'I';
    this.dependents = this.app.dependents;
  }

  numberOnly(event) {
    this.app.numberOnly(event);
  }

  _removeUndefined(obj: Object) {
    return this.app.removeUndefined(obj);
  }

  onSubmit(form: NgForm) {
    this.loading = true;
    this.response = null;
    let data = this._removeUndefined(form.value)
    this.appService.requestData('compare/clt', data).subscribe((result) => {
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
