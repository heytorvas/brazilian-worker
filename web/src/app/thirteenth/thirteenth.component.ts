import { Component, OnInit } from '@angular/core';
import { AppComponent } from '../app.component';
import { ThirteenthService } from './thirteenth.service';
import { Thirteenth } from './thirteenth.model';
import { NgForm } from '@angular/forms';

@Component({
  selector: 'app-thirteenth',
  templateUrl: './thirteenth.component.html',
  styleUrls: ['./thirteenth.component.css']
})
export class ThirteenthComponent implements OnInit {

  salary: Thirteenth = {} as Thirteenth;
  response!: Thirteenth | null;
  dependents;
  months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

  loading: boolean = false;

  constructor(private thirteenth: ThirteenthService, private app: AppComponent) { }

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
    this.thirteenth.getSalary(form.value).subscribe((result) => {
        this.loading = false;
        this.response = result;
    })
  }

}
