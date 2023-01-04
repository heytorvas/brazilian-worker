import { Component, OnInit } from '@angular/core';
import { NgForm } from '@angular/forms';
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

  constructor(private pjSalaryService: PJSalaryService) { }

  ngOnInit(): void {
    this.salary.attachment = 'I';
  }

  numberOnly(event): boolean {
    const charCode = (event.which) ? event.which : event.keyCode;
    if (charCode > 31 && (charCode < 48 || charCode > 57)) {
        return false;
    }
    return true;
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
