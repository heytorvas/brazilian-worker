import { Component, OnInit } from '@angular/core';
import { AppComponent } from '../app.component';
import { CompareOutputSchema } from '../compare.model';
import { CLTPJService } from './clt-pj.service';
import { NgForm } from '@angular/forms';
import { CLTPJSchema } from './clt-pj.model';

@Component({
  selector: 'app-clt-pj',
  templateUrl: './clt-pj.component.html',
  styleUrls: ['./clt-pj.component.css']
})
export class CltPjComponent implements OnInit {
  salary: CLTPJSchema = {} as CLTPJSchema;
  response!: CompareOutputSchema | null;
  dependents;

  loading: boolean = false;

  constructor(private service: CLTPJService, private app: AppComponent) { }

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
    this.service.getSalary(data).subscribe((result) => {
        this.loading = false;
        this.response = result;
    })
  }

}
