import { Component, OnInit } from '@angular/core';
import { NgForm } from '@angular/forms';
import { AppComponent } from '../app.component';
import { CompareOutputSchema } from '../compare.model';
import { PJSalaryBase } from '../pj-salary/pj-salary.model';
import { PJCLTService } from './pj-clt.service';

@Component({
  selector: 'app-pj-clt',
  templateUrl: './pj-clt.component.html',
  styleUrls: ['./pj-clt.component.css']
})
export class PjCltComponent implements OnInit {

  salary: PJSalaryBase = {} as PJSalaryBase;
  response!: CompareOutputSchema | null;

  loading: boolean = false;

  constructor(private pjCLTService: PJCLTService, private app: AppComponent) { }

  ngOnInit(): void {
    this.salary.attachment = 'I';
  }

  numberOnly(event) {
    this.app.numberOnly(event);
  }

  onSubmit(form: NgForm) {
    this.loading = true;
    this.response = null;
    this.pjCLTService.getSalary(form.value).subscribe((result) => {
        this.loading = false;
        this.response = result;
    })
  }

}
