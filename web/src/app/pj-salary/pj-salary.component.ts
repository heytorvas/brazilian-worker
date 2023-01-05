import { Component, OnInit } from '@angular/core';
import { NgForm } from '@angular/forms';
import { AppComponent } from '../app.component';
import { PJSalary, PJSalaryBase } from './pj-salary.model';
import { PJSalaryService } from './pj-salary.service';

@Component({
  selector: 'app-pj-salary',
  templateUrl: './pj-salary.component.html',
  styleUrls: ['./pj-salary.component.css']
})
export class PjSalaryComponent implements OnInit {

  salary: PJSalaryBase = {} as PJSalaryBase;
  response!: PJSalary | null;

  loading: boolean = false;

  constructor(private pjSalaryService: PJSalaryService, private app: AppComponent) { }

  ngOnInit(): void {
    this.salary.attachment = 'I';
  }

  numberOnly(event) {
    this.app.numberOnly(event);
  }

  onSubmit(form: NgForm) {
    this.loading = true;
    this.response = null;
    this.pjSalaryService.getSalary(form.value).subscribe((result) => {
        this.loading = false;
        this.response = result;
    })
  }
}
